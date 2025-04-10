import React from 'react';
import { Github, Mail, Twitter } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-tamil-blue-dark text-white py-10">
      <div className="container-custom text-center px-4">
        <div className="text-sm text-gray-300 space-y-4">
          <p className="leading-relaxed">
            &copy; {new Date().getFullYear()} <strong className="text-white">TamilKavi</strong>. Licensed under MIT.
            <br className="sm:hidden" />
            <span className="block sm:inline">
              All contributed poems belong to their respective authors.
            </span>
          </p>
          <p className="text-tamil-white font-medium text-base">
            Crafted with ❤️ & code by{' '}
            <a
              href="https://www.linkedin.com/in/anandsundaramoorthysa"
              target="_blank"
              rel="noopener noreferrer"
              className="underline text-tamil-gold decoration-tamil-gold/50 hover:text-white transition"
            >
              Anand Sundaramoorthy SA
            </a>
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
