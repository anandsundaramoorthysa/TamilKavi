import { useLocation, Link } from "react-router-dom";
import { useEffect } from "react";
import { ArrowLeftCircle, Contact, Mail } from "lucide-react";

const NotFound = () => {
  const location = useLocation();

  useEffect(() => {
    document.title = "404 Not Found | TamilKavi";
    window.scrollTo(0, 0);
    console.error(
      "🚫 404: Tried to access an unavailable route:",
      location.pathname
    );
  }, [location.pathname]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-100 to-gray-300 px-4 sm:px-6 py-16">
      <div className="max-w-md w-full text-center p-10 bg-white rounded-3xl shadow-2xl border border-gray-200 animate-fade-in">
        {/* Favicon display */}
        <div className="flex justify-center items-center mb-6">
          <div className="w-28 h-28 rounded-full overflow-hidden border-4 border-tamil-blue shadow-md">
            <img
              src="/favicon.ico"
              alt="TamilKavi Logo"
              className="w-full h-full object-cover"
            />
          </div>
        </div>

        {/* 404 */}
        <h1 className="text-6xl font-extrabold text-tamil-blue mb-2">404</h1>

        {/* Tamil quote */}
        <p className="italic text-sm text-tamil-gold mb-4">
          இங்கு நீங்கள் தேடும் பாதை இல்லை... நீங்கள் திரும்பி செல்வதற்கான வழியைக் நாங்கள் தருகிறோம்.
        </p>

        {/* Message */}
        <p className="text-lg text-gray-700 mb-6 leading-relaxed">
          The page you're looking for isn't available. Let us help you find your way back.
        </p>

        {/* Actions */}
        <div className="flex flex-col sm:flex-row justify-center gap-4">
          <Link
            to="/"
            className="inline-flex items-center justify-center bg-tamil-blue hover:bg-tamil-blue-dark text-white font-semibold px-6 py-3 rounded-full transition-all duration-300 shadow-lg"
            aria-label="Back to Home"
          >
            <ArrowLeftCircle className="mr-2 h-5 w-5" />
            Home
          </Link>

          <Link
            to="/team"
            className="inline-flex items-center justify-center bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium px-5 py-3 rounded-full transition duration-300 shadow-md"
            aria-label="Our Team"
          >
            <Contact className="mr-2 h-5 w-5" />
            Our Team
          </Link>
        </div>
      </div>
    </div>
  );
};

export default NotFound;
