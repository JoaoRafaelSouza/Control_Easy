// src/Views/template/Layout.tsx
import React from 'react';
import Header from './Header';
import Sidebar from './Sidebar';
import Footer from './Footer';

interface Props {
  children: React.ReactNode;
}

export default function Layout({ children }: Props) {
  return (
    <div className="d-flex flex-column min-vh-100">
      <Header />
      <div className="container-fluid flex-grow-1">
        <div className="row">
          <nav className="col-lg-2 d-none d-lg-block bg-light">
            <Sidebar />
          </nav>
          <main className="col-lg-10 col-12 p-4 bg-light">
            {children}
          </main>
        </div>
      </div>
      <Footer />
    </div>
  );
}