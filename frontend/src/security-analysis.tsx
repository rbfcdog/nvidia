"use client"

import NextLink from 'next/link'; 
import { useState, useRef } from 'react'
import { motion } from 'framer-motion'
import { Shield, Download, Loader2, User, Building, FileText, Network, Link as LinkIcon, Check, AlertCircle, UploadCloud, X, File, PlusCircle } from 'lucide-react'

// Define o tipo de estado da página
type FormState = 'initial' | 'loading' | 'finished'

export default function SecurityAnalysis() {
  const [formState, setFormState] = useState<FormState>('initial')
  const [files, setFiles] = useState<File[]>([])
  const [reportUrl, setReportUrl] = useState<string | null>(null); // Para armazenar a URL do relatório PDF
  const fileInputRef = useRef<HTMLInputElement>(null)

  const [currentYear] = useState(new Date().getFullYear())

  const resetForm = () => {
    setFormState('initial')
    setFiles([])
    setReportUrl(null)
  }

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      const newFiles = Array.from(event.target.files);
      setFiles(prevFiles => {
        const combined = [...prevFiles, ...newFiles];
        if (combined.length > 10) {
          alert("Você pode enviar no máximo 10 arquivos.");
          return combined.slice(0, 10);
        }
        return combined;
      });
    }
  }
  
  const handleRemoveFile = (indexToRemove: number) => {
    setFiles(prevFiles => prevFiles.filter((_, index) => index !== indexToRemove));
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (files.length === 0) {
      alert("Por favor, envie pelo menos um arquivo para análise.");
      return;
    }
  
    setFormState('loading');
  
    const formData = new FormData();
    files.forEach(file => {
      formData.append('files', file); // O backend receberá um array de 'files'
    });
  
    try {
      // Simulação de sucesso com um PDF fake
      console.log("Simulando upload e análise dos arquivos...");
      await new Promise(resolve => setTimeout(resolve, 5000)); // Simula 5s de processamento

      // Cria um PDF falso no navegador para o download de teste
      const fakePdfBlob = new Blob(["Este é um relatório de segurança simulado em PDF."], { type: 'application/pdf' });
      const fakePdfUrl = URL.createObjectURL(fakePdfBlob);
      setReportUrl(fakePdfUrl); // Armazena a URL do relatório gerado
      
      console.log("Simulação bem-sucedida! Relatório gerado.");
      setFormState('finished');

      /*
      // CÓDIGO REAL PARA QUANDO O BACKEND ESTIVER PRONTO
      const response = await fetch("/api/v1/analyze-files", {
        method: "POST",
        // IMPORTANTE: NÃO defina o header 'Content-Type', o navegador faz isso por você com FormData
        body: formData
      });
  
      if (!response.ok) {
        throw new Error(`Erro na requisição: ${response.statusText}`);
      }
  
      const reportBlob = await response.blob(); // O backend deve retornar o PDF como um blob
      const reportUrl = URL.createObjectURL(reportBlob);
      setReportUrl(reportUrl); // Armazena a URL do relatório real
      
      console.log("Análise concluída com sucesso! Relatório pronto para download.");
      setFormState('finished');
      */
  
    } catch (error) {
      console.error("Falha ao enviar os arquivos:", error);
      alert("Ocorreu um erro ao iniciar a análise. Tente novamente.");
      setFormState('initial');
    }
  };

  const handleDownload = () => {
    if (!reportUrl) return;

    const link = document.createElement('a');
    link.href = reportUrl;
    link.setAttribute('download', 'relatorio-de-seguranca.pdf'); // Nome do arquivo
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    // Não revogue a URL aqui se quiser permitir múltiplos downloads
  }

  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-b from-gray-900 to-black text-white relative overflow-hidden">
      <div 
        className="absolute inset-0 opacity-[0.015] pointer-events-none"
        style={{ backgroundImage: `url("data:image/svg+xml,...")` }}
      />

      <div className="container mx-auto px-4 py-12 max-w-2xl relative z-10 flex-grow">
        <motion.div initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="text-center mb-12">
          <NextLink href="/" className="inline-block group cursor-pointer">
            <div className="flex items-center justify-center mb-6">
              <Shield className="w-12 h-12 text-green-500 mr-4 group-hover:opacity-80 transition-opacity" />
              <div className="text-left">
                <h1 className="text-4xl font-bold text-white mb-2 group-hover:text-gray-200 transition-colors">
                  Console de Análise de Segurança
                </h1>
                <div className="h-0.5 bg-gradient-to-r from-green-500 to-transparent w-3/4"></div>
              </div>
            </div>
          </NextLink>
          <p className="text-gray-400 text-lg leading-relaxed max-w-3xl mx-auto">
            Faça o upload dos arquivos de log ou configuração (.txt) para que nossa plataforma orquestre os agentes de IA e execute as varreduras de segurança.
          </p>
        </motion.div>

        {/* File Upload Area */}
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.2 }} className="bg-gray-900/80 backdrop-blur-sm border border-gray-700 rounded-lg p-8 mb-8 shadow-2xl">
          {/* Hidden file input */}
          <input 
            type="file"
            ref={fileInputRef}
            onChange={handleFileChange}
            className="hidden"
            accept=".txt"
            multiple
            disabled={files.length >= 10}
          />

          {/* List of uploaded files */}
          {files.length > 0 && (
            <div className="space-y-3 mb-6">
              <h3 className="font-semibold text-gray-300">Arquivos Selecionados ({files.length}/10):</h3>
              {files.map((file, index) => (
                <motion.div 
                  key={index}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.3 }}
                  className="flex items-center justify-between bg-gray-800/50 p-3 rounded-lg border border-gray-600"
                >
                  <div className="flex items-center space-x-3">
                    <File className="w-5 h-5 text-green-500" />
                    <span className="text-sm text-white truncate">{file.name}</span>
                    <span className="text-xs text-gray-400">({(file.size / 1024).toFixed(2)} KB)</span>
                  </div>
                  <button onClick={() => handleRemoveFile(index)} className="text-gray-500 hover:text-red-500">
                    <X className="w-4 h-4" />
                  </button>
                </motion.div>
              ))}
            </div>
          )}

          {/* Upload Buttons */}
          <div className="flex flex-col sm:flex-row gap-4">
            <button
              onClick={() => fileInputRef.current?.click()}
              disabled={files.length >= 10}
              className="w-full flex items-center justify-center px-6 py-3 bg-gray-700 hover:bg-gray-600 disabled:bg-gray-800 disabled:cursor-not-allowed text-white font-medium rounded-lg transition-colors duration-300"
            >
              <UploadCloud className="w-5 h-5 mr-2" />
              {files.length === 0 ? 'Selecionar Arquivos' : 'Adicionar Mais Arquivos'}
            </button>
          </div>
        </motion.div>

        {/* Interactive Action Area */}
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.4 }} className="text-center">
          {formState === 'initial' && (
            <motion.button
              onClick={handleSubmit}
              disabled={files.length === 0}
              className="px-8 py-4 bg-green-500 hover:bg-green-600 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold rounded-lg transition-all duration-300 ease-in-out flex items-center justify-center mx-auto min-w-[200px] shadow-lg hover:shadow-xl transform hover:scale-105 disabled:hover:scale-100"
            >
              <Shield className="w-5 h-5 mr-2" />
              Executar Análise
            </motion.button>
          )}

          {formState === 'loading' && (
            <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="flex flex-col items-center space-y-4">
              <div className="flex items-center justify-center space-x-2">
                <Loader2 className="w-6 h-6 text-green-500 animate-spin" />
                <div className="flex space-x-1">
                  {/* Pulsating dots animation */}
                </div>
              </div>
              <p className="text-gray-400 text-lg">Executando varreduras...</p>
              <div className="bg-gray-800/50 backdrop-blur-sm rounded-lg p-4 max-w-md shadow-md">
                <p className="text-sm text-gray-300">Nossos agentes de IA estão orquestrando os testes com base nos arquivos enviados...</p>
              </div>
            </motion.div>
          )}

          {formState === 'finished' && (
            <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} className="flex flex-col items-center space-y-4">
              <motion.div initial={{ scale: 0 }} animate={{ scale: 1 }} transition={{ type: "spring", stiffness: 200, damping: 10 }} className="w-16 h-16 bg-green-500 rounded-full flex items-center justify-center mb-4 shadow-lg">
                <Shield className="w-8 h-8 text-white" />
              </motion.div>
              <div className="text-center mb-6">
                <h3 className="text-xl font-semibold text-white mb-2">Análise Concluída!</h3>
                <p className="text-gray-400">O relatório em PDF está pronto para download.</p>
              </div>
              <div className="flex flex-col space-y-3 w-full max-w-xs">
                <motion.button onClick={handleDownload} className="px-8 py-4 bg-green-500 hover:bg-green-600 text-white font-semibold rounded-lg flex items-center justify-center shadow-lg">
                  <Download className="w-5 h-5 mr-2" />
                  Baixar Relatório (PDF)
                </motion.button>
                <motion.button onClick={resetForm} className="px-8 py-4 bg-gray-700 hover:bg-gray-600 text-white font-medium rounded-lg flex items-center justify-center shadow-md">
                  <Shield className="w-5 h-5 mr-2" />
                  Nova Análise
                </motion.button>
              </div>
            </motion.div>
          )}
        </motion.div>
      </div>

      <footer className="bg-gray-900/90 backdrop-blur-sm border-t border-gray-700 text-gray-400 py-4 mt-12">
        <div className="container mx-auto px-4 text-center">
          <p className="text-sm mb-2">© {currentYear} CyberOps Copilot</p>
          <div className="flex justify-center space-x-6 text-xs">
            <a href="#" className="text-gray-500 hover:text-gray-300">Termos de Serviço</a>
            <a href="#" className="text-gray-500 hover:text-gray-300">Política de Privacidade</a>
          </div>
        </div>
      </footer>
    </div>
  )
}