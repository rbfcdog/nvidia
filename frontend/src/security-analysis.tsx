"use client"

import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Shield, Download, Loader2, User, Building, FileText, Network, Link, Check, AlertCircle, Lock } from 'lucide-react'

// Form data type
interface FormData {
  employeeName: string
  companyName: string
  cnpj: string
  targetIP: string
  systemURL: string
}

// Validation state type
interface ValidationState {
  employeeName: boolean
  companyName: boolean
  cnpj: boolean
  targetIP: boolean
  systemURL: boolean
}

// Form state type
type FormState = 'initial' | 'loading' | 'finished'

export default function SecurityAnalysis() {
  const [formState, setFormState] = useState<FormState>('initial')
  const [formData, setFormData] = useState<FormData>({
    employeeName: '',
    companyName: '',
    cnpj: '',
    targetIP: '',
    systemURL: ''
  })
  
  const [validation, setValidation] = useState<ValidationState>({
    employeeName: false,
    companyName: false,
    cnpj: false,
    targetIP: false,
    systemURL: false
  })

  const [currentYear] = useState(new Date().getFullYear())

  const resetForm = () => {
    setFormState('initial')
    setFormData({
      employeeName: '',
      companyName: '',
      cnpj: '',
      targetIP: '',
      systemURL: ''
    })
    setValidation({
      employeeName: false,
      companyName: false,
      cnpj: false,
      targetIP: false,
      systemURL: false
    })
  }

  // Validation functions
  const validateField = (field: keyof FormData, value: string): boolean => {
    switch (field) {
      case 'employeeName':
        return value.trim().length >= 2
      case 'companyName':
        return value.trim().length >= 2
      case 'cnpj':
        return /^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/.test(value) || value.replace(/\D/g, '').length === 14
      case 'targetIP':
        return /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(value)
      case 'systemURL':
        try {
          new URL(value)
          return true
        } catch {
          return false
        }
      default:
        return false
    }
  }

  const handleInputChange = (field: keyof FormData, value: string) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }))

    // Real-time validation
    const isValid = validateField(field, value)
    setValidation(prev => ({
      ...prev,
      [field]: isValid
    }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    // Start loading state
    setFormState('loading')
    
    // Simulate analysis process (7 seconds)
    setTimeout(() => {
      setFormState('finished')
    }, 60000)
  }

  const handleDownload = () => {
    // Simulate report download
    console.log('Downloading report...', formData)
  }

  const isFormValid = Object.values(formData).every(value => value.trim() !== '') && 
                     Object.values(validation).every(valid => valid)

  // Form fields configuration
  const formFields = [
    {
      id: 'employeeName',
      label: 'Nome do Funcionário',
      placeholder: 'Digite o nome completo',
      icon: User,
      type: 'text'
    },
    {
      id: 'companyName',
      label: 'Nome da Empresa',
      placeholder: 'Digite o nome da empresa',
      icon: Building,
      type: 'text'
    },
    {
      id: 'cnpj',
      label: 'CNPJ',
      placeholder: '00.000.000/0000-00',
      icon: FileText,
      type: 'text'
    },
    {
      id: 'targetIP',
      label: 'Endereço IP do Alvo',
      placeholder: '192.168.1.1',
      icon: Network,
      type: 'text'
    },
    {
      id: 'systemURL',
      label: 'URL do Sistema Web',
      placeholder: 'https://exemplo.com',
      icon: Link,
      type: 'url'
    }
  ]

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-black text-white relative overflow-hidden">
      {/* Subtle noise texture overlay */}
      <div 
        className="absolute inset-0 opacity-[0.015] pointer-events-none"
        style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E")`,
        }}
      />

      <div className="container mx-auto px-4 py-12 max-w-2xl relative z-10">
        {/* Header and Description */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <div className="flex items-center justify-center mb-6">
            <Shield className="w-12 h-12 text-green-500 mr-4" />
            <div className="text-left">
              <h1 className="text-4xl font-bold text-white mb-2">
                Simulador de Análise de Segurança
              </h1>
              {/* Green accent line */}
              <div className="h-0.5 bg-gradient-to-r from-green-500 to-transparent w-3/4"></div>
            </div>
          </div>
          
          <p className="text-gray-400 text-lg leading-relaxed max-w-3xl mx-auto">
            Preencha os dados abaixo para iniciar uma análise de vulnerabilidades no seu sistema. 
            Nossa orquestra de IA realizará testes de segurança e gerará um relatório detalhado.
          </p>
        </motion.div>

        {/* Input Form */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="bg-gray-900/80 backdrop-blur-sm border border-gray-700 rounded-lg p-8 mb-8 shadow-2xl"
        >
          <form onSubmit={handleSubmit} className="space-y-6">
            {formFields.map((field) => {
              const fieldKey = field.id as keyof FormData
              const IconComponent = field.icon
              const isValid = validation[fieldKey]
              const hasValue = formData[fieldKey].trim() !== ''
              
              return (
                <div key={field.id}>
                  <label htmlFor={field.id} className="block text-sm font-medium text-gray-300 mb-2 flex items-center">
                    <IconComponent className="w-4 h-4 text-gray-400 mr-2" />
                    {field.label}
                  </label>
                  <div className="relative">
                    <input
                      type={field.type}
                      id={field.id}
                      value={formData[fieldKey]}
                      onChange={(e) => handleInputChange(fieldKey, e.target.value)}
                      disabled={formState !== 'initial'}
                      className="w-full px-4 py-3 pr-12 bg-gray-800/50 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:border-green-500 focus:ring-1 focus:ring-green-500 transition-all duration-300 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed shadow-md"
                      placeholder={field.placeholder}
                      required
                    />
                    
                    {/* Validation icon */}
                    {hasValue && (
                      <div className="absolute right-3 top-1/2 transform -translate-y-1/2">
                        {isValid ? (
                          <Check className="w-5 h-5 text-green-500" />
                        ) : (
                          <AlertCircle className="w-5 h-5 text-red-500" />
                        )}
                      </div>
                    )}
                  </div>
                  
                  {/* Validation message */}
                  {hasValue && !isValid && (
                    <motion.p
                      initial={{ opacity: 0, y: -10 }}
                      animate={{ opacity: 1, y: 0 }}
                      className="text-red-400 text-sm mt-1 flex items-center"
                    >
                      <AlertCircle className="w-3 h-3 mr-1" />
                      {field.id === 'cnpj' && 'CNPJ deve ter formato válido'}
                      {field.id === 'targetIP' && 'IP deve ter formato válido (ex: 192.168.1.1)'}
                      {field.id === 'systemURL' && 'URL deve ser válida (ex: https://exemplo.com)'}
                      {(field.id === 'employeeName' || field.id === 'companyName') && 'Mínimo 2 caracteres'}
                    </motion.p>
                  )}
                </div>
              )
            })}
          </form>
        </motion.div>

        {/* Interactive Action Area */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="text-center"
        >
          {/* Initial State - Submit Button */}
          {formState === 'initial' && (
            <motion.button
              onClick={handleSubmit}
              disabled={!isFormValid}
              className="px-8 py-4 bg-green-500 hover:bg-green-600 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold rounded-lg transition-all duration-300 ease-in-out flex items-center justify-center mx-auto min-w-[200px] shadow-lg hover:shadow-xl transform hover:scale-105 disabled:hover:scale-100"
              whileHover={isFormValid ? { scale: 1.05 } : {}}
              whileTap={isFormValid ? { scale: 0.95 } : {}}
            >
              <Shield className="w-5 h-5 mr-2" />
              Iniciar Análise
            </motion.button>
          )}

          {/* Loading State */}
          {formState === 'loading' && (
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="flex flex-col items-center space-y-4"
            >
              <div className="flex items-center justify-center space-x-2">
                <Loader2 className="w-6 h-6 text-green-500 animate-spin" />
                <div className="flex space-x-1">
                  <motion.div
                    className="w-2 h-2 bg-green-500 rounded-full"
                    animate={{ scale: [1, 1.2, 1] }}
                    transition={{ duration: 1, repeat: Infinity, delay: 0 }}
                  />
                  <motion.div
                    className="w-2 h-2 bg-green-500 rounded-full"
                    animate={{ scale: [1, 1.2, 1] }}
                    transition={{ duration: 1, repeat: Infinity, delay: 0.20 }}
                  />
                  <motion.div
                    className="w-2 h-2 bg-green-500 rounded-full"
                    animate={{ scale: [1, 1.2, 1] }}
                    transition={{ duration: 1, repeat: Infinity, delay: 0.4 }}
                  />
                </div>
              </div>
              <p className="text-gray-400 text-lg">
                Analisando... Por favor, aguarde.
              </p>
              <div className="bg-gray-800/50 backdrop-blur-sm rounded-lg p-4 max-w-md shadow-md">
                <p className="text-sm text-gray-300">
                  Nossa IA está executando testes de segurança em tempo real...
                </p>
              </div>
            </motion.div>
          )}

          {/* Finished State - Two Buttons */}
          {formState === 'finished' && (
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="flex flex-col items-center space-y-4"
            >
              <motion.div
                className="w-16 h-16 bg-green-500 rounded-full flex items-center justify-center mb-4 shadow-lg"
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ type: "spring", stiffness: 200, damping: 10 }}
              >
                <Shield className="w-8 h-8 text-white" />
              </motion.div>
              
              <div className="text-center mb-6">
                <h3 className="text-xl font-semibold text-white mb-2">
                  Análise Concluída!
                </h3>
                <p className="text-gray-400">
                  Seu relatório de segurança está pronto para download.
                </p>
              </div>

              <div className="flex flex-col space-y-3 w-full max-w-xs">
                {/* Primary Button - Download Report */}
                <motion.button
                  onClick={handleDownload}
                  className="px-8 py-4 bg-green-500 hover:bg-green-600 border-2 border-green-500 hover:border-green-600 text-white font-semibold rounded-lg transition-all duration-300 ease-in-out flex items-center justify-center shadow-lg hover:shadow-xl transform hover:scale-105"
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Download className="w-5 h-5 mr-2" />
                  Baixar Relatório
                </motion.button>

                {/* Secondary Button - New Analysis */}
                <motion.button
                  onClick={resetForm}
                  className="px-8 py-4 bg-gray-700 hover:bg-gray-600 border-2 border-gray-600 hover:border-gray-500 text-white font-medium rounded-lg transition-all duration-300 ease-in-out flex items-center justify-center shadow-md hover:shadow-lg transform hover:scale-105"
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Shield className="w-5 h-5 mr-2" />
                  Realizar Nova Análise
                </motion.button>
              </div>
            </motion.div>
          )}
        </motion.div>

        {/* Progress Indicator */}
        {formState === 'loading' && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mt-8"
          >
            <div className="bg-gray-800/50 backdrop-blur-sm rounded-lg p-4 shadow-md">
              <div className="flex justify-between text-sm text-gray-400 mb-2">
                <span>Progresso da Análise</span>
                <span>Executando...</span>
              </div>
              <div className="w-full bg-gray-700 rounded-full h-2">
                <motion.div
                  className="bg-gradient-to-r from-green-500 to-green-400 h-2 rounded-full shadow-sm"
                  initial={{ width: "0%" }}
                  animate={{ width: "100%" }}
                  transition={{ duration: 60, ease: "easeInOut" }}
                />
              </div>
            </div>
          </motion.div>
        )}
      </div>

      {/* Fixed Footer */}
      <footer className="bg-gray-900/90 backdrop-blur-sm border-t border-gray-700 text-gray-400 py-4 mt-12">
        <div className="container mx-auto px-4 text-center">
          <p className="text-sm mb-2">
            © {currentYear} AI Defense Orchestra
          </p>
          <div className="flex justify-center space-x-6 text-xs">
            <a 
              href="#" 
              className="text-gray-500 hover:text-gray-300 transition-colors duration-300 ease-in-out"
            >
              Termos de Serviço
            </a>
            <a 
              href="#" 
              className="text-gray-500 hover:text-gray-300 transition-colors duration-300 ease-in-out"
            >
              Política de Privacidade
            </a>
          </div>
        </div>
      </footer>
    </div>
  )
}
