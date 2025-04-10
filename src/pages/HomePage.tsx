
import React from 'react';
import { Link } from 'react-router-dom';
import { Book, Github, Heart, Search } from 'lucide-react';

const HomePage = () => {
  return (
    <>
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-tamil-blue to-tamil-blue-dark text-white py-20">
        <div className="container-custom">
          <div className="flex flex-col items-center text-center">
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold mb-4 text-white">
              Tamil<span className="text-tamil-gold">Kavi</span>!
            </h1>
            <p className="text-xl md:text-2xl mb-8 max-w-2xl tamil-text">
              Free & open-source Tamil kavithai collection. Contribute pannunga, inspire pannunga!
            </p>
            <div className="flex flex-wrap gap-4 justify-center">
              <a 
                href="https://github.com/anandsundaramoorthysa/TamilKavi" 
                target="_blank"
                rel="noopener noreferrer"
                className="btn-secondary flex items-center"
              >
                <Github className="mr-2 h-5 w-5" />
                View on GitHub
              </a>
              <Link to="/submit" className="btn-primary flex items-center">
                <Heart className="mr-2 h-5 w-5" />
                Contribute a Kavithai
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <h2 className="text-3xl font-bold text-center mb-12">Project Features</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="bg-white p-6 rounded-lg shadow-md flex flex-col items-center text-center">
              <div className="bg-tamil-blue/10 p-4 rounded-full mb-4">
                <Book className="h-8 w-8 text-tamil-blue" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Rich Collection</h3>
              <p className="text-gray-600">
                Access a growing library of Tamil poems from various authors and time periods.
              </p>
            </div>
            
            <div className="bg-white p-6 rounded-lg shadow-md flex flex-col items-center text-center">
              <div className="bg-tamil-red/10 p-4 rounded-full mb-4">
                <Search className="h-8 w-8 text-tamil-red" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Easily Accessible</h3>
              <p className="text-gray-600">
                Available as a Python package and web resource for developers, researchers, and poetry lovers.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Sample Poem Section */}
      <section className="py-16">
        <div className="container-custom">
          <h2 className="text-3xl font-bold text-center mb-12">Featured Kavithai</h2>
          
          <div className="max-w-2xl mx-auto poem-container">
            <div className="mb-4">
              <h3 className="text-xl font-semibold">வாழ்க நிரந்தரம்</h3>
              <p className="text-sm text-gray-500">By Bharathiyar</p>
            </div>
            
            <div className="space-y-2 poem-line text-center">
              <p>வாழ்க நிரந்தரம் வாழ்க தமிழ்மொழி</p>
              <p>வாழிய வாழியவே!</p>
              <p>ஊழி தோறூழி உலகமுடனளாய்</p>
              <p>ஓங்குக ஓங்குகவே!</p>
            </div>
            
            <div className="mt-4 text-right">
              <Link to="/preview" className="text-tamil-blue hover:text-tamil-blue-dark font-medium">
                Read more poems →
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-tamil-earth-light">
        <div className="container-custom text-center">
          <h2 className="text-3xl font-bold mb-6">Join the Movement</h2>
          <p className="text-lg mb-8 max-w-2xl mx-auto">
            Help us preserve and promote Tamil literature by contributing your favorite poems or your original work.
          </p>
          <div className="flex flex-wrap gap-4 justify-center">
            <Link to="/contribute" className="btn-primary">
              Learn How to Contribute
            </Link>
            <Link to="/submit" className="btn-secondary">
              Submit a Poem Now
            </Link>
          </div>
        </div>
      </section>
    </>
  );
};

export default HomePage;
