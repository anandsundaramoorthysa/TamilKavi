import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { PenTool, Users, BookOpen, Code, HeartHandshake, Terminal } from 'lucide-react';

const AboutPage = () => {
  useEffect(() => {
    document.title = 'About | TamilKavi';
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="py-12">
      <div className="container-custom">
        <h1 className="text-4xl font-bold text-center mb-12">About the Project</h1>

        <div className="max-w-4xl mx-auto">
          {/* What is TamilKavi? */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-4">TamilKaviனா என்ன?</h2>
            <p className="text-lg mb-4">
              TamilKavi ஒரு open-source முயற்சி. புதுப் புது தமிழ் கவிஞர்களோட கவிதைகளை சேகரிக்கவும், உபயோகிக்கவும் இந்த project உருவாக்கப்பட்டுள்ளது.
              இந்த Python package மூலமாக, அந்த கவிதைகளை website/app development, AI/ML training, research-க்கு பயன்படுத்தலாம். தமிழ் இலக்கியத்தில் புதிய
              குரல்களை ஒரு Python package-க்குள் கொண்டு வருவதுதான் இந்த முயற்சியின் முக்கிய நோக்கம்!
            </p>
          </div>

          {/* Who Can Benefit from TamilKavi? */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-6">யாரெல்லாம் பயன்படுத்தலாம்?</h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Aspiring Poets */}
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex">
                <div className="mr-4">
                  <div className="bg-tamil-blue/10 p-3 rounded-full">
                    <PenTool className="h-6 w-6 text-tamil-blue" />
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-semibold mb-2">புதிய கவிஞர்கள்</h3>
                  <p className="text-gray-600">
                    உங்க சொந்த தமிழ் கவிதைகளை உலகத்துடன் பகிரலாம். Python மூலமா ஒரு digital format-ல் உங்க படைப்புகள் சேரும் – இது உங்களுக்கு ஒரு recognition-ம் கிடைக்க வாய்ப்பு.
                  </p>
                </div>
              </div>

              {/* Literary Enthusiasts */}
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex">
                <div className="mr-4">
                  <div className="bg-tamil-blue/10 p-3 rounded-full">
                    <Users className="h-6 w-6 text-tamil-blue" />
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-semibold mb-2">கவிதை ரசிகர்கள்</h3>
                  <p className="text-gray-600">
                    புதுசா எழுதப்பட்ட தமிழ் கவிதைகளை browse பண்ணலாம். Rasigaraga, புதிய மனநிலைகள், பாணிகள், emotions எல்லாமே இங்கே கிடைக்கும்!
                  </p>
                </div>
              </div>

              {/* Educators and Students */}
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex">
                <div className="mr-4">
                  <div className="bg-tamil-blue/10 p-3 rounded-full">
                    <BookOpen className="h-6 w-6 text-tamil-blue" />
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-semibold mb-2">ஆசிரியர்களும் மாணவர்களும்</h3>
                  <p className="text-gray-600">
                    Project work, literary analysis, class presentations-க்கு இப்போது real-world Tamil content-ஐ use பண்ணலாம். Modern Tamil literature-ஐ படிக்க நல்ல resource!
                  </p>
                </div>
              </div>

              {/* Developers and Researchers */}
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex">
                <div className="mr-4">
                  <div className="bg-tamil-blue/10 p-3 rounded-full">
                    <Terminal className="h-6 w-6 text-tamil-blue" />
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-semibold mb-2">Developers & Researchers</h3>
                  <p className="text-gray-600">
                    Web / App development, AI / ML dataset creation, NLP experimentation, chatbot training – நிறையவே கற்றல் + creative use-cases இருக்குது.
                    Custom Tamil datasets தேவைப்பட்ற இடத்தில், இந்த package perfect-a set ஆகும்.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Our Vision */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-4">எங்களோட கனவு</h2>
            <p className="text-lg">
              பாரம்பரிய தமிழ் இலக்கியத்தையும், இன்றைய software technology-யில் முக்கிய பங்கு வகிக்கும் Python-ஐயும் இணைக்கும் ஒரு digital மேடையா TamilKavi உருவாகணும் என்பது
              எங்களோட நோக்கம். இனிமே, Python package-களில் கூட புது கவிஞர்களின் கவிதைகளை பார்ப்பதும், அவற்றை பலவிதமான முறைகளில் உபயோகிப்பதும் சாத்தியமாகணும்.
            </p>
          </div>

          {/* Want to Contribute? */}
          <div className="bg-tamil-earth-light p-8 rounded-lg">
            <div className="flex flex-col md:flex-row items-center">
              <div className="md:w-1/2 mb-6 md:mb-0">
                <HeartHandshake className="h-24 w-24 mx-auto text-tamil-earth-dark" />
              </div>
              <div className="md:w-1/2">
                <h3 className="text-xl font-bold mb-3">நீங்களும் சேரலாமே!</h3>
                <p className="mb-4">
                  உங்க சொந்த கவிதையை Python package-க்குள் சேர்க்கணும்-னு ஆசை இருக்கா? இல்லேனா, இவ்வளவு அழகான முயற்சிக்கு support பண்ணணும்-னு தோணுதா? TamilKavi உங்களை பாசத்தோட வரவேற்குது!
                </p>
                <Link to="/contribute" className="btn-primary inline-block">
                  Learn How to Contribute
                </Link>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};

export default AboutPage;
