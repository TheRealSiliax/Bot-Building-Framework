/**
 * Main Application Entry Point
 * Initialisiert alle Module und Event-Listener
 */

import { initNavigation } from './components/navigation.js';
import { initChatbot } from './components/chatbot.js';
import { initWaveBackground } from './components/waveBackground.js';

/**
 * Initialisiert die Anwendung wenn das DOM geladen ist
 */
document.addEventListener('DOMContentLoaded', () => {
    console.log('Website initialisiert');
    
    // Wave Background initialisieren (WebGL Sonnenuntergang)
    const waveBackground = initWaveBackground('waveCanvas', {
        mouseInfluence: 1.0,
        enableTouch: true,
        respectReducedMotion: true
    });
    
    // Navigation initialisieren
    initNavigation();
    
    // Chatbot initialisieren
    initChatbot();
    
    // Kontaktformular initialisieren
    initContactForm();
});

/**
 * Initialisiert das Kontaktformular
 */
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    
    if (!contactForm) return;
    
    contactForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        
        const formData = new FormData(contactForm);
        const data = Object.fromEntries(formData.entries());
        
        console.log('Formular abgesendet:', data);
        
        // Hier könnte die Formular-Verarbeitung implementiert werden
        alert('Vielen Dank für Ihre Nachricht! Wir melden uns bald bei Ihnen.');
        contactForm.reset();
    });
}

