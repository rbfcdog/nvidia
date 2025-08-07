'use client'

import Link from 'next/link';
import { Inter } from 'next/font/google'
import { ChevronDown } from 'lucide-react'
import { motion } from 'framer-motion'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <div className={inter.className}>
      {/* Hero Section with Green Theme */}
      <main className="min-h-screen bg-gradient-to-br from-green-900 via-emerald-900 to-green-950 relative overflow-hidden" style={{
        backgroundImage: `radial-gradient(circle at 25% 25%, rgba(34, 197, 94, 0.1) 0%, transparent 50%), 
                         radial-gradient(circle at 75% 75%, rgba(16, 185, 129, 0.1) 0%, transparent 50%)`
      }}>
        {/* Subtle texture overlay */}
        <div className="absolute inset-0 opacity-20">
          <div className="absolute inset-0 bg-gradient-to-r from-transparent via-green-500/5 to-transparent"></div>
          <div className="absolute inset-0 bg-gradient-to-b from-transparent via-emerald-500/5 to-transparent"></div>
        </div>
        
        {/* Animated background elements */}
        <div className="absolute inset-0">
          <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-green-500/10 rounded-full blur-3xl animate-pulse"></div>
          <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl animate-pulse delay-1000"></div>
          <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-green-600/5 rounded-full blur-3xl animate-pulse delay-500"></div>
        </div>

        {/* Main content */}
        <div className="relative z-10 flex flex-col items-center justify-center min-h-screen px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-5xl mx-auto">
            {/* Main heading */}
            <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold text-green-400 mb-6 leading-tight animate-fade-in">
              Onde a Inteligência Artificial se Torna sua{' '}
              <span className="bg-gradient-to-r from-green-300 to-emerald-300 bg-clip-text text-transparent">
                Linha de Frente
              </span>{' '}
              na Defesa.
            </h1>

            {/* Subheading */}
            <h2 className="text-lg sm:text-xl md:text-2xl lg:text-3xl text-green-400 mb-12 leading-relaxed max-w-4xl mx-auto animate-fade-in-delay">
              AI Defense Orchestra: Automatize, antecipe e neutralize ameaças antes que elas aconteçam.
            </h2>

            {/* Optional CTA buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center mb-16 animate-fade-in-delay-2">
              <Link href="/page2">
                <button className="px-8 py-4 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-lg hover:from-green-700 hover:to-emerald-700 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
                  Começar Agora
                </button>
              </Link>
              <Link href="/page2">
                <button className="px-8 py-4 border border-green-600 text-green-300 font-semibold rounded-lg hover:border-green-500 hover:text-white transition-all duration-300 transform hover:scale-105">
                  Saiba Mais
                </button>
                </Link>
            </div>
          </div>

          {/* Scroll indicator */}
          <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
            <div className="flex flex-col items-center text-green-400 hover:text-green-300 transition-colors duration-300 cursor-pointer">
              <span className="text-sm mb-2 font-medium">Role para baixo</span>
              <ChevronDown className="w-6 h-6 animate-pulse text-green-400" />
            </div>
          </div>
        </div>
      </main>

      {/* Traditional Cybersecurity Challenges Section */}
      <section className="bg-slate-950 py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          {/* Section Title */}
          <div className="text-center mb-16">
            <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-white mb-6 leading-tight animate-on-scroll">
              A cibersegurança tradicional não acompanha a{' '}
              <span className="bg-gradient-to-r from-red-400 to-orange-400 bg-clip-text text-transparent">
                velocidade das ameaças
              </span>.
            </h2>
          </div>

          {/* Two Column Layout */}
          <div className="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
            {/* Left Column - Text Blocks */}
            <div className="space-y-8">
              {/* Custos Elevados */}
              <div className="animate-on-scroll-delay-1 bg-slate-900/50 p-6 rounded-lg border border-slate-800 hover:border-slate-700 transition-colors duration-300">
                <h3 className="text-xl sm:text-2xl font-bold text-white mb-4 flex items-center">
                  <div className="w-2 h-2 bg-red-500 rounded-full mr-3"></div>
                  Custos Elevados
                </h3>
                <p className="text-gray-300 leading-relaxed">
                  Soluções tradicionais exigem grandes equipes especializadas e infraestrutura complexa, 
                  gerando custos operacionais que crescem exponencialmente com a escala.
                </p>
              </div>

              {/* Fadiga de Alertas */}
              <div className="animate-on-scroll-delay-2 bg-slate-900/50 p-6 rounded-lg border border-slate-800 hover:border-slate-700 transition-colors duration-300">
                <h3 className="text-xl sm:text-2xl font-bold text-white mb-4 flex items-center">
                  <div className="w-2 h-2 bg-orange-500 rounded-full mr-3"></div>
                  Fadiga de Alertas
                </h3>
                <p className="text-gray-300 leading-relaxed">
                  Milhares de falsos positivos sobrecarregam as equipes de segurança, 
                  causando burnout e reduzindo a eficácia na detecção de ameaças reais.
                </p>
              </div>

              {/* Janela de Exposição */}
              <div className="animate-on-scroll-delay-3 bg-slate-900/50 p-6 rounded-lg border border-slate-800 hover:border-slate-700 transition-colors duration-300">
                <h3 className="text-xl sm:text-2xl font-bold text-white mb-4 flex items-center">
                  <div className="w-2 h-2 bg-yellow-500 rounded-full mr-3"></div>
                  Janela de Exposição
                </h3>
                <p className="text-gray-300 leading-relaxed">
                  O tempo entre detecção e resposta permite que atacantes se movam lateralmente, 
                  causando danos irreversíveis antes da contenção.
                </p>
              </div>
            </div>

            {/* Right Column - Placeholder for Image/Animation */}
            <div className="animate-on-scroll-delay-4">
              <div className="relative h-96 lg:h-[500px] bg-gradient-to-br from-slate-800 to-slate-900 rounded-lg border-2 border-dashed border-slate-600 flex items-center justify-center overflow-hidden">
                {/* Animated background pattern */}
                <div className="absolute inset-0 opacity-10">
                  <div className="absolute top-4 left-4 w-8 h-8 border border-red-500 rounded animate-pulse"></div>
                  <div className="absolute top-12 right-8 w-6 h-6 border border-orange-500 rounded animate-pulse delay-300"></div>
                  <div className="absolute bottom-16 left-8 w-10 h-10 border border-yellow-500 rounded animate-pulse delay-700"></div>
                  <div className="absolute bottom-8 right-12 w-4 h-4 border border-red-500 rounded animate-pulse delay-1000"></div>
                  <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-16 h-16 border border-orange-500 rounded animate-pulse delay-500"></div>
                </div>
                
                {/* Center content */}
                <div className="text-center z-10">
                  <div className="w-24 h-24 mx-auto mb-4 bg-gradient-to-br from-red-500/20 to-orange-500/20 rounded-full flex items-center justify-center border border-red-500/30">
                    <div className="w-12 h-12 bg-gradient-to-br from-red-500 to-orange-500 rounded-full animate-pulse"></div>
                  </div>
                  <p className="text-gray-400 text-sm">
                    Visualização Conceitual
                  </p>
                  <p className="text-gray-500 text-xs mt-1">
                    Ameaças em Tempo Real
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* AI Orchestra Process Section */}
      <section className="bg-slate-900 min-h-screen">
        <div className="max-w-7xl mx-auto">
          <div className="grid lg:grid-cols-2 min-h-screen">
            {/* Left Column - Sticky Title */}
            <div className="lg:sticky lg:top-0 lg:h-screen flex items-center justify-center p-8 lg:p-16">
              <div className="text-center lg:text-left">
                <h2 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold text-white leading-tight">
                  Nossa{' '}
                  <span className="bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
                    Orquestra de IA
                  </span>
                  : Precisão, Coordenação e Inteligência.
                </h2>
              </div>
            </div>

            {/* Right Column - Scrolling Step Cards */}
            <div className="space-y-0">
              {/* Step 1 */}
              <motion.div
                initial={{ opacity: 0, y: 100 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, ease: "easeOut" }}
                viewport={{ once: true, amount: 0.3 }}
                className="min-h-screen flex items-center p-8 lg:p-16"
              >
                <div className="w-full">
                  <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-8 border border-slate-700 shadow-2xl">
                    <div className="flex items-center mb-6">
                      <div className="w-12 h-12 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full flex items-center justify-center text-white font-bold text-xl mr-4">
                        1
                      </div>
                      <h3 className="text-2xl sm:text-3xl font-bold text-white">
                        Criamos sua Equipe de Elite.
                      </h3>
                    </div>
                    <p className="text-gray-300 text-lg leading-relaxed mb-8">
                      Nossa IA recruta e treina especialistas virtuais em diferentes domínios de segurança, 
                      cada um com expertise específica em detecção, análise e resposta a ameaças.
                    </p>
                    
                    {/* Visual Placeholder */}
                    <div className="h-64 bg-gradient-to-br from-blue-500/10 to-cyan-500/10 rounded-lg border border-blue-500/20 flex items-center justify-center relative overflow-hidden">
                      <div className="absolute inset-0 bg-gradient-to-r from-blue-500/5 to-cyan-500/5"></div>
                      <div className="grid grid-cols-3 gap-4 z-10">
                        <div className="w-16 h-16 bg-blue-500/20 rounded-full border border-blue-500/40 animate-pulse"></div>
                        <div className="w-16 h-16 bg-cyan-500/20 rounded-full border border-cyan-500/40 animate-pulse delay-300"></div>
                        <div className="w-16 h-16 bg-purple-500/20 rounded-full border border-purple-500/40 animate-pulse delay-700"></div>
                      </div>
                      <div className="absolute bottom-4 right-4 text-xs text-gray-500">
                        Equipe de IA Especializada
                      </div>
                    </div>
                  </div>
                </div>
              </motion.div>

              {/* Step 2 */}
              <motion.div
                initial={{ opacity: 0, y: 100 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, ease: "easeOut", delay: 0.2 }}
                viewport={{ once: true, amount: 0.3 }}
                className="min-h-screen flex items-center p-8 lg:p-16"
              >
                <div className="w-full">
                  <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-8 border border-slate-700 shadow-2xl">
                    <div className="flex items-center mb-6">
                      <div className="w-12 h-12 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full flex items-center justify-center text-white font-bold text-xl mr-4">
                        2
                      </div>
                      <h3 className="text-2xl sm:text-3xl font-bold text-white">
                        O Maestro entra em Ação.
                      </h3>
                    </div>
                    <p className="text-gray-300 text-lg leading-relaxed mb-8">
                      Um sistema central coordena toda a orquestra, distribuindo tarefas, 
                      sincronizando análises e garantindo que cada especialista trabalhe em harmonia perfeita.
                    </p>
                    
                    {/* Visual Placeholder */}
                    <div className="h-64 bg-gradient-to-br from-purple-500/10 to-pink-500/10 rounded-lg border border-purple-500/20 flex items-center justify-center relative overflow-hidden">
                      <div className="absolute inset-0 bg-gradient-to-r from-purple-500/5 to-pink-500/5"></div>
                      <div className="relative z-10">
                        <div className="w-20 h-20 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full flex items-center justify-center mb-4 animate-pulse">
                          <div className="w-8 h-8 bg-white rounded-full"></div>
                        </div>
                        <div className="flex space-x-2 justify-center">
                          <div className="w-2 h-8 bg-purple-500/60 rounded animate-pulse"></div>
                          <div className="w-2 h-12 bg-pink-500/60 rounded animate-pulse delay-200"></div>
                          <div className="w-2 h-6 bg-purple-500/60 rounded animate-pulse delay-400"></div>
                          <div className="w-2 h-10 bg-pink-500/60 rounded animate-pulse delay-600"></div>
                        </div>
                      </div>
                      <div className="absolute bottom-4 right-4 text-xs text-gray-500">
                        Coordenação Central
                      </div>
                    </div>
                  </div>
                </div>
              </motion.div>

              {/* Step 3 */}
              <motion.div
                initial={{ opacity: 0, y: 100 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, ease: "easeOut", delay: 0.4 }}
                viewport={{ once: true, amount: 0.3 }}
                className="min-h-screen flex items-center p-8 lg:p-16"
              >
                <div className="w-full">
                  <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-8 border border-slate-700 shadow-2xl">
                    <div className="flex items-center mb-6">
                      <div className="w-12 h-12 bg-gradient-to-r from-green-500 to-emerald-500 rounded-full flex items-center justify-center text-white font-bold text-xl mr-4">
                        3
                      </div>
                      <h3 className="text-2xl sm:text-3xl font-bold text-white">
                        A Simulação de Defesa Começa.
                      </h3>
                    </div>
                    <p className="text-gray-300 text-lg leading-relaxed mb-8">
                      Cada agente de IA simula cenários de ataque em tempo real, 
                      testando defesas e identificando vulnerabilidades antes que sejam exploradas.
                    </p>
                    
                    {/* Visual Placeholder */}
                    <div className="h-64 bg-gradient-to-br from-green-500/10 to-emerald-500/10 rounded-lg border border-green-500/20 flex items-center justify-center relative overflow-hidden">
                      <div className="absolute inset-0 bg-gradient-to-r from-green-500/5 to-emerald-500/5"></div>
                      <div className="grid grid-cols-4 gap-2 z-10">
                        {[...Array(16)].map((_, i) => (
                          <div
                            key={i}
                            className="w-8 h-8 bg-green-500/20 border border-green-500/40 rounded animate-pulse"
                            style={{ animationDelay: `${i * 100}ms` }}
                          ></div>
                        ))}
                      </div>
                      <div className="absolute bottom-4 right-4 text-xs text-gray-500">
                        Simulação Ativa
                      </div>
                    </div>
                  </div>
                </div>
              </motion.div>

              {/* Step 4 */}
              <motion.div
                initial={{ opacity: 0, y: 100 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, ease: "easeOut", delay: 0.6 }}
                viewport={{ once: true, amount: 0.3 }}
                className="min-h-screen flex items-center p-8 lg:p-16"
              >
                <div className="w-full">
                  <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-8 border border-slate-700 shadow-2xl">
                    <div className="flex items-center mb-6">
                      <div className="w-12 h-12 bg-gradient-to-r from-orange-500 to-red-500 rounded-full flex items-center justify-center text-white font-bold text-xl mr-4">
                        4
                      </div>
                      <h3 className="text-2xl sm:text-3xl font-bold text-white">
                        De Ruído a Relatórios Acionáveis.
                      </h3>
                    </div>
                    <p className="text-gray-300 text-lg leading-relaxed mb-8">
                      Transformamos milhares de alertas em insights precisos e recomendações claras, 
                      eliminando falsos positivos e priorizando ameaças reais.
                    </p>
                    
                    {/* Visual Placeholder */}
                    <div className="h-64 bg-gradient-to-br from-orange-500/10 to-red-500/10 rounded-lg border border-orange-500/20 flex items-center justify-center relative overflow-hidden">
                      <div className="absolute inset-0 bg-gradient-to-r from-orange-500/5 to-red-500/5"></div>
                      <div className="space-y-3 z-10 w-full max-w-xs">
                        <div className="h-4 bg-gradient-to-r from-orange-500/40 to-red-500/40 rounded animate-pulse"></div>
                        <div className="h-4 bg-gradient-to-r from-orange-500/60 to-red-500/60 rounded animate-pulse delay-200"></div>
                        <div className="h-4 bg-gradient-to-r from-orange-500/30 to-red-500/30 rounded animate-pulse delay-400"></div>
                        <div className="h-6 bg-gradient-to-r from-orange-500 to-red-500 rounded animate-pulse delay-600"></div>
                      </div>
                      <div className="absolute bottom-4 right-4 text-xs text-gray-500">
                        Relatórios Inteligentes
                      </div>
                    </div>
                  </div>
                </div>
              </motion.div>
            </div>
          </div>
        </div>
      </section>

      {/* Benefits Section with Purple Theme */}
      <section className="bg-slate-950 py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          {/* Section Title */}
          <div className="text-center mb-16">
            <motion.h2 
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, ease: "easeOut" }}
              viewport={{ once: true, amount: 0.3 }}
              className="text-3xl sm:text-4xl md:text-5xl font-bold text-white mb-6 leading-tight"
            >
              O que sua empresa ganha com uma{' '}
              <span className="bg-gradient-to-r from-purple-400 to-violet-400 bg-clip-text text-transparent">
                Orquestra de Defesa
              </span>?
            </motion.h2>
          </div>

          {/* Benefits Grid */}
          <div className="grid md:grid-cols-3 gap-8">
            {/* Benefit 1 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, ease: "easeOut", delay: 0.1 }}
              viewport={{ once: true, amount: 0.3 }}
              className="bg-slate-900/50 p-8 rounded-xl border border-purple-800/30 hover:border-purple-600/50 hover:shadow-lg hover:shadow-purple-500/20 transition-all duration-300 group"
            >
              {/* Icon Placeholder */}
              <div className="w-16 h-16 bg-gradient-to-br from-purple-500 to-violet-500 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                <div className="w-8 h-8 bg-white rounded opacity-90"></div>
              </div>
              
              <h3 className="text-xl sm:text-2xl font-bold text-white mb-4">
                Redução Drástica de Custos
              </h3>
              <p className="text-gray-300 leading-relaxed">
                Elimine a necessidade de grandes equipes especializadas. Nossa IA automatiza 90% das tarefas de segurança, 
                reduzindo custos operacionais em até 70% enquanto aumenta a eficácia.
              </p>
            </motion.div>

            {/* Benefit 2 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, ease: "easeOut", delay: 0.3 }}
              viewport={{ once: true, amount: 0.3 }}
              className="bg-slate-900/50 p-8 rounded-xl border border-purple-800/30 hover:border-purple-600/50 hover:shadow-lg hover:shadow-purple-500/20 transition-all duration-300 group"
            >
              {/* Icon Placeholder */}
              <div className="w-16 h-16 bg-gradient-to-br from-purple-500 to-violet-500 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                <div className="w-8 h-8 bg-white rounded opacity-90"></div>
              </div>
              
              <h3 className="text-xl sm:text-2xl font-bold text-white mb-4">
                Velocidade de Detecção 10x Maior
              </h3>
              <p className="text-gray-300 leading-relaxed">
                De horas para segundos. Nossa orquestra de IA identifica e responde a ameaças em tempo real, 
                fechando janelas de exposição antes que danos sejam causados.
              </p>
            </motion.div>

            {/* Benefit 3 */}
            <motion.div
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, ease: "easeOut", delay: 0.5 }}
              viewport={{ once: true, amount: 0.3 }}
              className="bg-slate-900/50 p-8 rounded-xl border border-purple-800/30 hover:border-purple-600/50 hover:shadow-lg hover:shadow-purple-500/20 transition-all duration-300 group"
            >
              {/* Icon Placeholder */}
              <div className="w-16 h-16 bg-gradient-to-br from-purple-500 to-violet-500 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                <div className="w-8 h-8 bg-white rounded opacity-90"></div>
              </div>
              
              <h3 className="text-xl sm:text-2xl font-bold text-white mb-4">
                Inteligência, Não Apenas Dados
              </h3>
              <p className="text-gray-300 leading-relaxed">
                Transformamos o caos de alertas em insights acionáveis. Receba apenas o que importa, 
                com contexto completo e recomendações precisas para cada situação.
              </p>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Technology Stack Section with Official Logos */}
      <section className="bg-slate-900 py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          {/* Section Title */}
          <div className="text-center mb-16">
            <motion.h2 
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, ease: "easeOut" }}
              viewport={{ once: true, amount: 0.3 }}
              className="text-3xl sm:text-4xl md:text-5xl font-bold text-white mb-6 leading-tight"
            >
              Construído sobre uma{' '}
              <span className="bg-gradient-to-r from-green-400 to-emerald-400 bg-clip-text text-transparent">
                Fundação de Inovação
              </span>
            </motion.h2>
          </div>

          {/* Technology Stack Visualization */}
          <div className="flex items-center justify-center min-h-[500px] relative">
            {/* Main Central NVIDIA Logo */}
            <motion.div
              initial={{ opacity: 0, scale: 0.5 }}
              whileInView={{ opacity: 1, scale: 1 }}
              transition={{ duration: 1, ease: "easeOut" }}
              viewport={{ once: true, amount: 0.3 }}
              className="w-32 h-32 bg-white rounded-2xl flex items-center justify-center relative z-10 shadow-2xl"
              style={{
                boxShadow: '0 0 50px rgba(34, 197, 94, 0.4), 0 0 100px rgba(34, 197, 94, 0.2)',
              }}
            >
              <img 
                src="/placeholder.svg?height=80&width=120&text=NVIDIA" 
                alt="NVIDIA Logo" 
                className="w-20 h-12 object-contain"
              />
            </motion.div>

            {/* Surrounding Technology Logos */}
            {[
              { 
                angle: 0, 
                delay: 0.2, 
                tooltip: "CrewAI: Orquestra a colaboração entre agentes de IA especializados",
                logo: "CrewAI",
                bgColor: "from-blue-600 to-blue-700"
              },
              { 
                angle: 120, 
                delay: 0.4, 
                tooltip: "Docker: Containerização para deploy escalável e consistente",
                logo: "Docker",
                bgColor: "from-blue-500 to-cyan-500"
              },
              { 
                angle: 240, 
                delay: 0.6, 
                tooltip: "Python: Linguagem principal para desenvolvimento de IA e automação",
                logo: "Python",
                bgColor: "from-yellow-500 to-blue-500"
              }
            ].map((tech, index) => {
              const radius = 150;
              const x = Math.cos((tech.angle * Math.PI) / 180) * radius;
              const y = Math.sin((tech.angle * Math.PI) / 180) * radius;
              
              return (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, scale: 0 }}
                  whileInView={{ opacity: 1, scale: 1 }}
                  whileHover={{ scale: 1.2 }}
                  transition={{ duration: 0.8, ease: "easeOut", delay: tech.delay }}
                  viewport={{ once: true, amount: 0.3 }}
                  className={`absolute w-20 h-20 bg-gradient-to-br ${tech.bgColor} rounded-xl flex items-center justify-center cursor-pointer group shadow-lg`}
                  style={{
                    transform: `translate(${x}px, ${y}px)`,
                  }}
                >
                  <img 
                    src={`/placeholder-40x40.png?height=40&width=40&text=${tech.logo}`} 
                    alt={`${tech.logo} Logo`} 
                    className="w-10 h-10 object-contain filter brightness-0 invert"
                  />
                  
                  {/* Tooltip */}
                  <div className="absolute -top-16 left-1/2 transform -translate-x-1/2 bg-slate-800 text-white px-4 py-2 rounded-lg text-sm whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none max-w-xs text-center shadow-xl border border-slate-700">
                    {tech.tooltip}
                    <div className="absolute top-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-4 border-r-4 border-t-4 border-transparent border-t-slate-800"></div>
                  </div>
                </motion.div>
              );
            })}

            {/* Connection Lines */}
            <svg className="absolute inset-0 w-full h-full pointer-events-none" style={{ zIndex: 1 }}>
              {[0, 120, 240].map((angle, index) => {
                const radius = 150;
                const x1 = 50; // Center percentage
                const y1 = 50; // Center percentage
                const x2 = 50 + (Math.cos((angle * Math.PI) / 180) * radius) / 5; // Adjust for percentage
                const y2 = 50 + (Math.sin((angle * Math.PI) / 180) * radius) / 5; // Adjust for percentage
                
                return (
                  <motion.line
                    key={index}
                    initial={{ pathLength: 0, opacity: 0 }}
                    whileInView={{ pathLength: 1, opacity: 0.3 }}
                    transition={{ duration: 1.5, ease: "easeOut", delay: 0.8 + index * 0.2 }}
                    viewport={{ once: true, amount: 0.3 }}
                    x1={`${x1}%`}
                    y1={`${y1}%`}
                    x2={`${x2}%`}
                    y2={`${y2}%`}
                    stroke="rgb(34, 197, 94)"
                    strokeWidth="2"
                    strokeDasharray="5,5"
                  />
                );
              })}
            </svg>
          </div>
        </div>
      </section>

      {/* Call to Action Section */}
      <section className="bg-slate-950 py-24 px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            viewport={{ once: true, amount: 0.3 }}
          >
            <h1 className="text-4xl sm:text-5xl md:text-6xl font-bold text-white mb-8 leading-tight">
              Pronto para{' '}
              <span className="bg-gradient-to-r from-green-400 to-emerald-400 bg-clip-text text-transparent">
                revolucionar
              </span>{' '}
              sua segurança?
            </h1>
            
            <p className="text-xl sm:text-2xl text-gray-300 mb-12 leading-relaxed max-w-3xl mx-auto">
              Descubra como nossa Orquestra de IA pode transformar sua postura de segurança em questão de semanas, 
              não meses. Comece com uma simulação personalizada para sua empresa.
            </p>
            
            <Link href="/page2">
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="px-12 py-6 bg-gradient-to-r from-green-500 to-emerald-500 text-white font-bold text-xl rounded-xl shadow-lg hover:shadow-xl hover:shadow-green-500/25 transition-all duration-300"
                style={{
                  boxShadow: '0 10px 30px rgba(34, 197, 94, 0.3)'
                }}
              >
                Iniciar Simulação de Segurança
              </motion.button>
            </Link>
          </motion.div>
        </div>
      </section>

      <style jsx>{`
        @keyframes fade-in {
          from {
            opacity: 0;
            transform: translateY(30px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @keyframes slide-in-left {
          from {
            opacity: 0;
            transform: translateX(-50px);
          }
          to {
            opacity: 1;
            transform: translateX(0);
          }
        }

        @keyframes slide-in-right {
          from {
            opacity: 0;
            transform: translateX(50px);
          }
          to {
            opacity: 1;
            transform: translateX(0);
          }
        }

        .animate-fade-in {
          animation: fade-in 1s ease-out;
        }

        .animate-fade-in-delay {
          animation: fade-in 1s ease-out 0.3s both;
        }

        .animate-fade-in-delay-2 {
          animation: fade-in 1s ease-out 0.6s both;
        }

        .animate-on-scroll {
          opacity: 0;
          animation: fade-in 0.8s ease-out 0.2s both;
        }

        .animate-on-scroll-delay-1 {
          opacity: 0;
          animation: slide-in-left 0.8s ease-out 0.4s both;
        }

        .animate-on-scroll-delay-2 {
          opacity: 0;
          animation: slide-in-left 0.8s ease-out 0.6s both;
        }

        .animate-on-scroll-delay-3 {
          opacity: 0;
          animation: slide-in-left 0.8s ease-out 0.8s both;
        }

        .animate-on-scroll-delay-4 {
          opacity: 0;
          animation: slide-in-right 0.8s ease-out 1s both;
        }
      `}</style>
    </div>
  )
}
