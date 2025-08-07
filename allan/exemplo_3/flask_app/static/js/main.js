document.addEventListener('DOMContentLoaded', function() {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const fileSelectBtn = document.getElementById('file-select-btn');
    const fileList = document.getElementById('file-list');
    const filesUl = document.getElementById('files');
    const uploadBtn = document.getElementById('upload-btn');
    const clearBtn = document.getElementById('clear-btn');
    const progressSection = document.getElementById('progress-section');
    const resultsSection = document.getElementById('results-section');
    const analyzeBtn = document.getElementById('analyze-btn');
    
    let selectedFiles = [];
    let currentSessionId = null;

    // File selection button
    fileSelectBtn.addEventListener('click', () => {
        fileInput.click();
    });

    // File input change
    fileInput.addEventListener('change', (e) => {
        handleFiles(e.target.files);
    });

    // Drag and drop events
    dropZone.addEventListener('click', () => {
        fileInput.click();
    });

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        handleFiles(e.dataTransfer.files);
    });

    // Clear files
    clearBtn.addEventListener('click', () => {
        selectedFiles = [];
        fileInput.value = '';
        updateFileList();
    });

    // Upload files
    uploadBtn.addEventListener('click', () => {
        uploadFiles();
    });

    // Start analysis
    analyzeBtn.addEventListener('click', () => {
        startAnalysis();
    });

    function handleFiles(files) {
        const allowedTypes = ['txt', 'log', 'xml', 'json', 'csv', 'nmap', 'scan'];
        
        Array.from(files).forEach(file => {
            const extension = file.name.split('.').pop().toLowerCase();
            if (allowedTypes.includes(extension)) {
                // Check if file already exists
                if (!selectedFiles.find(f => f.name === file.name && f.size === file.size)) {
                    selectedFiles.push(file);
                }
            } else {
                alert(`File type .${extension} is not supported. Please use: ${allowedTypes.join(', ')}`);
            }
        });

        updateFileList();
    }

    function updateFileList() {
        if (selectedFiles.length === 0) {
            fileList.style.display = 'none';
            return;
        }

        fileList.style.display = 'block';
        filesUl.innerHTML = '';

        selectedFiles.forEach((file, index) => {
            const li = document.createElement('li');
            li.innerHTML = `
                <span>${file.name} (${formatFileSize(file.size)})</span>
                <button onclick="removeFile(${index})" style="float: right; background: none; border: none; color: #e53e3e; cursor: pointer;">✕</button>
            `;
            filesUl.appendChild(li);
        });
    }

    function removeFile(index) {
        selectedFiles.splice(index, 1);
        updateFileList();
    }

    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    function uploadFiles() {
        if (selectedFiles.length === 0) {
            alert('Please select files to upload');
            return;
        }

        const formData = new FormData();
        selectedFiles.forEach(file => {
            formData.append('files[]', file);
        });

        progressSection.style.display = 'block';
        updateProgress(0, 'Uploading files...');

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            
            currentSessionId = data.session_id;
            updateProgress(100, 'Files uploaded successfully!');
            
            setTimeout(() => {
                progressSection.style.display = 'none';
                resultsSection.style.display = 'block';
            }, 1000);
        })
        .catch(error => {
            alert('Upload failed: ' + error.message);
            progressSection.style.display = 'none';
        });
    }

    function startAnalysis() {
        if (!currentSessionId) {
            alert('No session available. Please upload files first.');
            return;
        }

        fetch(`/analyze/${currentSessionId}`, {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            
            // Redirect to results page
            window.location.href = `/results/${currentSessionId}`;
        })
        .catch(error => {
            alert('Failed to start analysis: ' + error.message);
        });
    }

    function updateProgress(percent, text) {
        const progressFill = document.getElementById('progress-fill');
        const progressText = document.getElementById('progress-text');
        
        progressFill.style.width = percent + '%';
        progressText.textContent = text;
    }

    // Make removeFile globally available
    window.removeFile = removeFile;
});