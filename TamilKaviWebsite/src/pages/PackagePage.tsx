import React, { useEffect } from 'react';
import { Clipboard, Code, CopyCheck, Database, Download, Package } from 'lucide-react';
import { useState } from 'react';

const PackagePage = () => {
  useEffect(() => {
    document.title = 'Package | TamilKavi';
    window.scrollTo(0, 0);
  }, []);
  const [copied, setCopied] = useState<Record<string, boolean>>({
    install: false,
    import: false,
    usage: false
  });
  
  const copyToClipboard = (text: string, key: string) => {
    navigator.clipboard.writeText(text);
    setCopied({ ...copied, [key]: true });
    setTimeout(() => {
      setCopied({ ...copied, [key]: false });
    }, 3000);
  };

  return (
    <div className="py-12">
      <div className="container-custom">
        <h1 className="text-4xl font-bold text-center mb-6">Package Information</h1>
        <p className="text-lg text-center mb-12 max-w-3xl mx-auto">
          TamilKavi is available as an open-source Python package, making it easy to integrate 
          Tamil poems into your applications, research, or creative projects.
        </p>
        
        <div className="max-w-3xl mx-auto">
          {/* Package Details */}
          <div className="bg-white rounded-lg shadow-sm border border-gray-100 p-8 mb-10">
            <div className="flex items-center mb-6">
              <div className="bg-tamil-blue/10 p-3 rounded-full mr-4">
                <Package className="h-6 w-6 text-tamil-blue" />
              </div>
              <h2 className="text-2xl font-bold">tamil-kavithaigal</h2>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <p className="text-sm text-gray-500 mb-1">Current Version</p>
                <p className="font-semibold">0.1.0</p>
              </div>
              <div>
                <p className="text-sm text-gray-500 mb-1">License</p>
                <p className="font-semibold">MIT</p>
              </div>
              <div>
                <p className="text-sm text-gray-500 mb-1">Release Date</p>
                <p className="font-semibold">April 10, 2023</p>
              </div>
              <div>
                <p className="text-sm text-gray-500 mb-1">Python Version</p>
                <p className="font-semibold">3.6+</p>
              </div>
            </div>
          </div>
          
          {/* Installation */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-4 flex items-center">
              <Download className="mr-2 h-6 w-6" />
              Installation
            </h2>
            <p className="mb-4">
              Install the package using pip:
            </p>
            
            <div className="relative">
              <pre className="bg-gray-800 text-green-400 p-4 rounded-md overflow-x-auto">
                pip install tamil-kavithaigal
              </pre>
              <button
                onClick={() => copyToClipboard('pip install tamil-kavithaigal', 'install')}
                className="absolute top-2 right-2 bg-gray-700 hover:bg-gray-600 text-white p-2 rounded-md"
                aria-label="Copy to clipboard"
              >
                {copied.install ? <CopyCheck className="h-4 w-4" /> : <Clipboard className="h-4 w-4" />}
              </button>
            </div>
          </div>
          
          {/* Usage Examples */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-4 flex items-center">
              <Code className="mr-2 h-6 w-6" />
              Usage Examples
            </h2>
            
            <div className="space-y-6">
              <div>
                <h3 className="text-lg font-semibold mb-2">Basic Import</h3>
                <div className="relative">
                  <pre className="bg-gray-800 text-green-400 p-4 rounded-md overflow-x-auto">
                    from tamil_kavithaigal import get_poem
                  </pre>
                  <button
                    onClick={() => copyToClipboard('from tamil_kavithaigal import get_poem', 'import')}
                    className="absolute top-2 right-2 bg-gray-700 hover:bg-gray-600 text-white p-2 rounded-md"
                    aria-label="Copy to clipboard"
                  >
                    {copied.import ? <CopyCheck className="h-4 w-4" /> : <Clipboard className="h-4 w-4" />}
                  </button>
                </div>
              </div>
              
              <div>
                <h3 className="text-lg font-semibold mb-2">Get a Random Poem</h3>
                <div className="relative">
                  <pre className="bg-gray-800 text-green-400 p-4 rounded-md overflow-x-auto">
{`# Get random poem
poem = get_poem()
print(poem['title'])
print(poem['content'])

# Get random poem by author
poem = get_poem(author="Bharathiyar")
print(poem['title'])
print(poem['content'])`}
                  </pre>
                  <button
                    onClick={() => copyToClipboard(`# Get random poem
poem = get_poem()
print(poem['title'])
print(poem['content'])

# Get random poem by author
poem = get_poem(author="Bharathiyar")
print(poem['title'])
print(poem['content'])`, 'usage')}
                    className="absolute top-2 right-2 bg-gray-700 hover:bg-gray-600 text-white p-2 rounded-md"
                    aria-label="Copy to clipboard"
                  >
                    {copied.usage ? <CopyCheck className="h-4 w-4" /> : <Clipboard className="h-4 w-4" />}
                  </button>
                </div>
              </div>
            </div>
          </div>
          
          {/* Additional Features */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-6">Additional Features</h2>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
                <h3 className="text-lg font-semibold mb-2">List Available Authors</h3>
                <pre className="bg-gray-100 p-3 rounded-md overflow-x-auto text-xs md:text-sm">
{`from tamil_kavithaigal import list_authors

authors = list_authors()
print(authors)  # ['Bharathiyar', 'Kannadasan', ...]`}
                </pre>
              </div>
              
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
                <h3 className="text-lg font-semibold mb-2">Search Poems</h3>
                <pre className="bg-gray-100 p-3 rounded-md overflow-x-auto text-xs md:text-sm">
{`from tamil_kavithaigal import search_poems

results = search_poems("தமிழ்")
for poem in results:
    print(poem['title'])`}
                </pre>
              </div>
              
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
                <h3 className="text-lg font-semibold mb-2">Get All Poems by Author</h3>
                <pre className="bg-gray-100 p-3 rounded-md overflow-x-auto text-xs md:text-sm">
{`from tamil_kavithaigal import get_poems_by_author

poems = get_poems_by_author("Avvaiyar")
for poem in poems:
    print(poem['title'])`}
                </pre>
              </div>
              
              <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
                <h3 className="text-lg font-semibold mb-2">Export to JSON</h3>
                <pre className="bg-gray-100 p-3 rounded-md overflow-x-auto text-xs md:text-sm">
{`from tamil_kavithaigal import export_to_json

export_to_json("bharathiyar_poems.json", 
               author="Bharathiyar")`}
                </pre>
              </div>
            </div>
          </div>
          
          {/* Data Structure */}
          <div className="mb-10">
            <h2 className="text-2xl font-bold mb-4 flex items-center">
              <Database className="mr-2 h-6 w-6" />
              Data Structure
            </h2>
            <p className="mb-4">
              The package follows a hierarchical data structure:
            </p>
            
            <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
              <pre className="bg-gray-100 p-4 rounded-md overflow-x-auto">
{`{
  "author": "Author Name",
  "contact": "Optional contact info",
  "books": [
    {
      "booktitle": "Book Title",
      "coverimage": "Optional cover image URL",
      "description": "Book description",
      "category": "Book category",
      "context": [
        {
          "title": "Poem Title",
          "line": "Poem content...",
          "meaning": "Optional translation or meaning"
        },
        // More poems...
      ]
    },
    // More books...
  ]
}`}
              </pre>
            </div>
          </div>
          
          <div className="bg-tamil-earth-light p-8 rounded-lg text-center">
            <h3 className="text-xl font-bold mb-4">Want to contribute to the package?</h3>
            <div className="flex flex-wrap gap-4 justify-center">
              <a 
                href="https://github.com/anandsundaramoorthysa/TamilKavi" 
                target="_blank"
                rel="noopener noreferrer"
                className="btn-primary"
              >
                Visit on GitHub
              </a>
              <a 
                href="https://pypi.org/project/tamil-kavithaigal/" 
                target="_blank"
                rel="noopener noreferrer"
                className="btn-secondary"
              >
                View on PyPI
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PackagePage;
