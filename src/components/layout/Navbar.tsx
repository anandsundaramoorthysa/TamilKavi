import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { cn } from '@/lib/utils';
import {
  Book, Github, Heart, Home, Info, Package, Send, Users, Menu, X
} from 'lucide-react';

const Navbar = () => {
  const location = useLocation();
  const [mobileOpen, setMobileOpen] = useState(false);

  const navItems = [
    { name: 'Home', path: '/', icon: <Home className="h-4 w-4 mr-1" /> },
    { name: 'About', path: '/about', icon: <Info className="h-4 w-4 mr-1" /> },
    { name: 'Contribute', path: '/contribute', icon: <Heart className="h-4 w-4 mr-1" /> },
    { name: 'Preview Poems', path: '/preview', icon: <Book className="h-4 w-4 mr-1" /> },
    { name: 'Package Info', path: '/package', icon: <Package className="h-4 w-4 mr-1" /> },
    { name: 'Team', path: '/team', icon: <Users className="h-4 w-4 mr-1" /> },
    { name: 'Submit', path: '/submit', icon: <Send className="h-4 w-4 mr-1" /> },
  ];

  return (
    <header className="bg-white shadow-sm">
      <div className="container-custom py-4">
        <div className="flex items-center justify-between">
          <Link to="/" className="flex items-center">
            <span className="text-2xl font-bold text-tamil-blue">
              Tamil<span className="text-tamil-gold">Kavi</span>!
            </span>
          </Link>

          {/* Desktop Nav */}
          <nav className="hidden md:flex items-center space-x-1">
            {navItems.map((item) => (
              <Link
                key={item.name}
                to={item.path}
                className={cn(
                  "px-3 py-2 rounded-md text-sm font-medium flex items-center",
                  location.pathname === item.path
                    ? "bg-tamil-blue text-white"
                    : "text-gray-700 hover:bg-tamil-blue/10 transition-colors"
                )}
              >
                {item.icon}
                {item.name}
              </Link>
            ))}
          </nav>

          {/* GitHub Link */}
          <a
            href="https://github.com/anandsundaramoorthysa/TamilKavi"
            target="_blank"
            rel="noopener noreferrer"
            className="hidden md:flex items-center text-gray-700 hover:text-tamil-blue transition-colors"
          >
            <Github className="h-5 w-5" />
            <span className="ml-2 hidden sm:inline">GitHub</span>
          </a>

          {/* Mobile Hamburger */}
          <button
            className="md:hidden text-gray-700"
            onClick={() => setMobileOpen(!mobileOpen)}
            aria-label="Toggle Menu"
          >
            {mobileOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>

        {/* Mobile Nav Panel */}
        {mobileOpen && (
          <div className="md:hidden mt-4 border-t pt-4 space-y-2">
            {navItems.map((item) => (
              <Link
                key={item.name}
                to={item.path}
                onClick={() => setMobileOpen(false)}
                className={cn(
                  "block px-4 py-2 rounded-md text-sm font-medium flex items-center",
                  location.pathname === item.path
                    ? "bg-tamil-blue text-white"
                    : "text-gray-700 hover:bg-tamil-blue/10 transition-colors"
                )}
              >
                {item.icon}
                {item.name}
              </Link>
            ))}
            <a
              href="https://github.com/anandsundaramoorthysa/TamilKavi"
              target="_blank"
              rel="noopener noreferrer"
              className="block px-4 py-2 text-sm font-medium text-gray-700 hover:text-tamil-blue transition-colors flex items-center"
            >
              <Github className="h-4 w-4 mr-1" />
              GitHub
            </a>
          </div>
        )}
      </div>
    </header>
  );
};

export default Navbar;
