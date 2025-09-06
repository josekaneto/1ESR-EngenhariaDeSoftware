"use client";
import { useState } from "react";
import ContactForm from "./componentes/ContactForm";
import ContactList from "./componentes/ContactList";

const HomePage = () => {
  const [contacts, setContacts] = useState([]);

  const handleSubmit = (newContact) => {
    setContacts(prev => [...prev, newContact]);
  };

  const handleRemove = (id) => {
    setContacts(prev => prev.filter(c => c.id !== id));
  };

  return (
    <div className="min-h-screen bg-gray-200 p-6">
      <div className="max-w-3xl mx-auto space-y-6">
        <header className="flex items-center justify-between">
          <h1 className="text-2xl font-bold text-gray-900">Cadastro de Contatos</h1>
          {/* Filtro entra aqui */}
        </header>

        <ContactForm onAdd={handleSubmit} />

        <ContactList items={contacts} onRemove={handleRemove} />
      </div>
    </div>
  );
};

export default HomePage;