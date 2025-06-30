// src/Views/template/Header.tsx
import React from 'react';

export default function Header() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-3">
      <a className="navbar-brand" href="#">Control Easy</a>
      <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#sidebarMenu">
        <span className="navbar-toggler-icon"></span>
      </button>
    </nav>
  );
}