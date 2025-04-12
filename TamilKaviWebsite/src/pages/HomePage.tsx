import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Book, Github, Heart, Search } from 'lucide-react';

const HomePage = () => {
  useEffect(() => {
    document.title = 'Home | TamilKavi';
    window.scrollTo(0, 0);
  }, []);

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
            Tamil-il codingum, kavithaiyum kalandhu oru pudhu ulagam-a kattrom pathu and use panni enjoy pannunga!
            </p>
            <div className="flex flex-wrap gap-4 justify-center">
              <a
                href="https://github.com/anandsundaramoorthysa/TamilKavi"
                target="_blank"
                rel="noopener noreferrer"
                className="btn-secondary flex items-center"
              >
                <Github className="mr-2 h-5 w-5" />
                GitHub-ல பாக்கலாம்
              </a>
              <Link to="/submit" className="btn-primary flex items-center">
                <Heart className="mr-2 h-5 w-5" />
                உங்க கவிதையைச் சேர்க்கவும்
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <h2 className="text-3xl font-bold text-center mb-12">எங்களோட சிறப்பம்சங்கள்</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="bg-white p-6 rounded-lg shadow-md flex flex-col items-center text-center">
              <div className="bg-tamil-blue/10 p-4 rounded-full mb-4">
                <Book className="h-8 w-8 text-tamil-blue" />
              </div>
              <h3 className="text-xl font-semibold mb-2">பண்பட்ட சேகரிப்பு</h3>
              <p className="text-gray-600">
                புதிய கவிஞர்களின் கவிதைகள் – காலத்தால் மாறாதவை.
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md flex flex-col items-center text-center">
              <div className="bg-tamil-red/10 p-4 rounded-full mb-4">
                <Search className="h-8 w-8 text-tamil-red" />
              </div>
              <h3 className="text-xl font-semibold mb-2">எளிதாக அணுகலாம்</h3>
              <p className="text-gray-600">
                இந்த package-ஐ நீங்க website / app development-க்கு, AI & ML training-க்கும் or any other purposeku use பண்ணலாம் – இல்லை என்றால் ஒரு rasigana ரசிக்கலாம்!
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-tamil-earth-light">
        <div className="container-custom text-center">
          <h2 className="text-3xl font-bold mb-6">இணைந்து கொள்ளுங்கள்</h2>
          <p className="text-lg mb-8 max-w-2xl mx-auto">
            தமிழ்மொழி இலக்கியத்தை பாதுகாக்கவும், உங்க கவிதையைப் பகிரவும், TamilKavi-யுடன் நீங்களும் வாருங்கள்.
          </p>
          <div className="flex flex-wrap gap-4 justify-center">
            <Link to="/contribute" className="btn-primary">
              எப்படி contribute பண்ணலாம்?
            </Link>
            <Link to="/submit" className="btn-secondary">
              இப்போதே கவிதைச் சேர்க்கவும்
            </Link>
          </div>
        </div>
      </section>
    </>
  );
};

export default HomePage;
