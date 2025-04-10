import React, {useEffect } from 'react';
import { Github, Globe, Mail, Twitter } from 'lucide-react';
import { FaLinkedin, FaTelegram, FaInstagram } from 'react-icons/fa';

interface TeamMember {
  name: string;
  role: string;
  github: string;
  linkedin?: string;
  telegram?: string;
  instagram?: string;
  website?: string;
  twitter?: string;
  email?: string;
  avatar: string;
  bio: string;
}

const teamMembers: TeamMember[] = [
  {
    name: 'Anand Sundaramoorthy SA',
    role: 'Developer & Prompt Engineer',
    github: 'anandsundaramoorthysa',
    linkedin: 'https://linkedin.com/in/anandsundaramoorthysa',
    telegram: 'https://t.me/anandsundaramoorthysa',
    instagram: 'https://instagram.com/anandsundaramoorthysa',
    website: 'https://anand.jigg.win',
    email: 'sanand03072005@gmail.com',
    avatar: 'https://media.licdn.com/dms/image/v2/D4D03AQEg7Gw6Qi6AdA/profile-displayphoto-shrink_800_800/B4DZTUmfrIGcAc-/0/1738733660369?e=1749686400&v=beta&t=gkxOE9ruFyZYeosoSsn8UfbiKIJlYiMQLF-8zuQZYUc',
    bio: 'LCM\'25 | Tech & Finance Enthusiast | Blog Writer | Developer & Prompt Engineer | Explore Which I Love'
  },
  {
    name: 'Booapalan S',
    role: 'Python Developer',
    github: 'boopalan-s',
    telegram: 'https://t.me/+917558147649',
    email: 'content.boopalan@gmail.com',
    avatar: 'https://gitlab.com/uploads/-/system/user/avatar/22134717/avatar.png',
    bio: 'I\'m a tech enthusiast who loves working with Python, open-source tools, and Linux systems.'
  }
];

const TeamPage = () => {
  useEffect(() => {
    document.title = 'Team | TamilKavi';
    window.scrollTo(0, 0);
  }, []);
  return (
    <div className="py-16 bg-gradient-to-br from-white via-gray-50 to-white">
      <div className="container-custom">
        <h1 className="text-4xl font-extrabold text-center text-tamil-blue-dark mb-4">
          Meet the Team
        </h1>
        <p className="text-lg text-center text-gray-600 mb-12 max-w-2xl mx-auto">
          The passionate individuals behind TamilKavi, blending code and culture to bring Tamil poetry to the world.
        </p>

        {/* Core Team */}
        <div className="max-w-4xl mx-auto mb-20">
          <h2 className="text-2xl font-semibold mb-8 text-center text-tamil-green-dark">
            Core Team
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {teamMembers.map((member) => (
              <div
                key={member.github}
                className="bg-white rounded-3xl shadow-md border border-gray-200 hover:shadow-xl transition-all duration-300 p-6 group hover:-translate-y-1"
              >
                <div className="flex flex-col items-center text-center">
                  <img
                    src={member.avatar}
                    alt={member.name}
                    className="w-24 h-24 rounded-full border-4 border-tamil-blue-dark object-cover mb-4 transition-transform group-hover:scale-105"
                  />
                  <h3 className="text-xl font-semibold text-gray-900">{member.name}</h3>
                  <p className="text-sm text-tamil-blue-dark mb-2">{member.role}</p>
                  <p className="text-sm text-gray-600 mb-4">{member.bio}</p>
                  <div className="flex gap-3 text-tamil-blue-dark justify-center flex-wrap">
                    {member.github && (
                      <a href={`https://github.com/${member.github}`} target="_blank" rel="noreferrer">
                        <Github className="h-5 w-5 hover:text-black" />
                      </a>
                    )}
                    {member.linkedin && (
                      <a href={member.linkedin} target="_blank" rel="noreferrer">
                        <FaLinkedin className="h-5 w-5 hover:text-[#0077b5]" />
                      </a>
                    )}
                    {member.telegram && (
                      <a href={member.telegram} target="_blank" rel="noreferrer">
                        <FaTelegram className="h-5 w-5 hover:text-[#0088cc]" />
                      </a>
                    )}
                    {member.instagram && (
                      <a href={member.instagram} target="_blank" rel="noreferrer">
                        <FaInstagram className="h-5 w-5 hover:text-pink-600" />
                      </a>
                    )}
                    {member.email && (
                      <a href={`mailto:${member.email}`}>
                        <Mail className="h-5 w-5 hover:text-red-500" />
                      </a>
                    )}
                    {member.twitter && (
                      <a href={member.twitter} target="_blank" rel="noreferrer">
                        <Twitter className="h-5 w-5 hover:text-[#1DA1F2]" />
                      </a>
                    )}
                    {member.website && (
                      <a href={member.website} target="_blank" rel="noreferrer">
                        <Globe className="h-5 w-5 hover:text-green-600" />
                      </a>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Contributors Section */}
        <div className="max-w-5xl mx-auto mb-20">
          <h2 className="text-2xl font-semibold mb-6 text-center text-tamil-gold-dark">
            Contributors
          </h2>
          <p className="text-center text-gray-700 mb-8 px-4">
            We’re grateful to the growing community of contributors who share their code, poems, and passion with TamilKavi.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            {[...Array(2)].map((_, i) => (
              <a
                key={i}
                href={`https://github.com/contributor${i}`}
                target="_blank"
                rel="noopener noreferrer"
                className="w-40 flex flex-col items-center text-center bg-white rounded-2xl shadow-sm border border-gray-200 hover:shadow-md transform hover:scale-[1.02] transition-all duration-300 p-4"
              >
                <img
                  src={`https://i.pravatar.cc/150?img=${i + 10}`}
                  alt={`Contributor ${i + 1}`}
                  className="w-20 h-20 rounded-full mb-2 shadow-sm object-cover"
                />
                <span className="text-sm font-medium text-gray-800 hover:text-tamil-blue transition-colors">
                  Contributor {i + 1}
                </span>
              </a>
            ))}
          </div>
        </div>

        {/* Join Us Section */}
        <div className="max-w-3xl mx-auto text-center py-12 px-6 bg-white/70 backdrop-blur-md border border-tamil-earth rounded-xl shadow">
          <h2 className="text-2xl font-semibold text-tamil-blue-dark mb-4">Join Our Mission</h2>
          <p className="text-base text-gray-700 mb-6">
            Whether you're a poet, developer, translator or an enthusiast, we’d love to have you onboard.
            Be a part of preserving and promoting Tamil literature in the digital age.
          </p>
          <div className="flex flex-wrap gap-4 justify-center">
            <a
              href="https://github.com/anandsundaramoorthysa/TamilKavi"
              target="_blank"
              rel="noopener noreferrer"
              className="btn-primary px-5 py-2 rounded-xl shadow hover:scale-105 transition bg-tamil-blue text-white font-medium"
            >
              Contribute on GitHub
            </a>
            <a
              href="mailto:sanand03072005@gmail.com"
              className="btn-secondary px-5 py-2 rounded-xl border border-tamil-blue text-tamil-blue hover:bg-tamil-blue/10 font-medium"
            >
              Contact Us
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TeamPage;
