import React from 'react';
import { Link } from 'react-router-dom';
import { PenTool, Users, BookOpen, Code, HeartHandshake, Terminal } from 'lucide-react';

const AboutPage = () => {
  return (
    <div className="py-12">
      <div className="container-custom">
        <h1 className="text-4xl font-bold text-center mb-12">About the Project</h1>

        <div className="max-w-4xl mx-auto">
          {/* What is TamilKavi? */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-4">What is TamilKavi?</h2>
            <p className="text-lg mb-4">
              TamilKavi is an open-source initiative dedicated to collecting and sharing contemporary Tamil poetry from emerging and lesser-known poets. Our goal is to provide a platform where new voices in Tamil literature can share their work with a global audience, fostering a vibrant community of modern Tamil poets and enthusiasts as a Python package.
            </p>
          </div>

          {/* Who Can Benefit from TamilKavi? */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-6">Who Can Benefit from TamilKavi?</h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Aspiring Poets */}
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex">
                <div className="mr-4">
                  <div className="bg-tamil-blue/10 p-3 rounded-full">
                    <PenTool className="h-6 w-6 text-tamil-blue" />
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-semibold mb-2">Aspiring Poets</h3>
                  <p className="text-gray-600">
                    Share your original Tamil poems with a wider audience and contribute to the growing landscape of contemporary Tamil literature.
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
                  <h3 className="text-lg font-semibold mb-2">Literary Enthusiasts</h3>
                  <p className="text-gray-600">
                    Discover fresh and modern Tamil poetry, exploring new themes and expressions from emerging authors.
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
                  <h3 className="text-lg font-semibold mb-2">Educators and Students</h3>
                  <p className="text-gray-600">
                    Access a diverse collection of recent Tamil poems for study, analysis, and appreciation in academic settings.
                  </p>
                </div>
              </div>

              {/* Project Developers */}
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100 flex">
                <div className="mr-4">
                  <div className="bg-tamil-blue/10 p-3 rounded-full">
                    <Terminal className="h-6 w-6 text-tamil-blue" />
                  </div>
                </div>
                <div>
                  <h3 className="text-lg font-semibold mb-2">Project Developers</h3>
                  <p className="text-gray-600">
                    Whether you're working on a web, app, AI, or ML project, access a curated collection of Tamil poems to enhance your work. The growth of this package relies on contributions, making it as expansive or concise as the community's involvement.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Our Vision */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-4">Our Vision</h2>
            <p className="text-lg">
              We envision TamilKavi as a dynamic repository that bridges traditional Tamil literary heritage with contemporary creative expressions. By providing an open-source platform for new Tamil poetry, we aim to nurture and promote the voices of today's poets, ensuring that Tamil literature continues to evolve and resonate with current and future generations.
            </p>
          </div>

          {/* Want to Contribute? */}
          <div className="bg-tamil-earth-light p-8 rounded-lg">
            <div className="flex flex-col md:flex-row items-center">
              <div className="md:w-1/2 mb-6 md:mb-0">
                <HeartHandshake className="h-24 w-24 mx-auto text-tamil-earth-dark" />
              </div>
              <div className="md:w-1/2">
                <h3 className="text-xl font-bold mb-3">Want to Contribute?</h3>
                <p className="mb-4">
                  TamilKavi thrives on community contributions. If you're an emerging Tamil poet looking to share your work, or if you're passionate about promoting contemporary Tamil literature, we welcome your involvement.
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
