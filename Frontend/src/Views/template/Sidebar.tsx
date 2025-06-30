// src/Views/template/Sidebar.tsx
import React from 'react';
import { Link } from 'react-router-dom';

export default function Sidebar() {
  return (
    <div className="collapse d-lg-block bg-light" id="sidebarMenu">
      <div className="list-group list-group-flush p-2">
        <Link to="/dashboard" className="list-group-item list-group-item-action">Dashboard</Link>
        <Link to="/usuarios" className="list-group-item list-group-item-action">Usuários</Link>
        {/* outros menus aqui */}
      </div>
    </div>
  );
}
