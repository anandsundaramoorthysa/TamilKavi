import React, { useState, useEffect } from 'react';
import { poemsData } from '../data/poems';
import { Search } from 'lucide-react';

const PreviewPage = () => {
  useEffect(() => {
    document.title = 'Preview | TamilKavi';
    window.scrollTo(0, 0);
  }, []);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterAuthor, setFilterAuthor] = useState('');
  
  // Get unique author names for filter dropdown
  const authors = Array.from(new Set(poemsData.map(author => author.author)));
  
  // Filter poems based on search term and author filter
  const filteredPoems = poemsData.filter(author => 
    (filterAuthor === '' || author.author === filterAuthor) &&
    (searchTerm === '' || 
      author.author.toLowerCase().includes(searchTerm.toLowerCase()) ||
      author.books.some(book => 
        book.booktitle.toLowerCase().includes(searchTerm.toLowerCase()) ||
        book.context.some(poem => 
          poem.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
          poem.line.toLowerCase().includes(searchTerm.toLowerCase())
        )
      )
    )
  );

  return (
    <div className="py-12">
      <div className="container-custom">
        <h1 className="text-4xl font-bold text-center mb-6">Preview Kavithaigal</h1>
        <p className="text-lg text-center mb-12 max-w-3xl mx-auto">
          Explore our collection of Tamil poems from various authors and time periods.
          Use the filters below to find specific poems.
        </p>
        
        {/* Search and Filter Controls */}
        <div className="max-w-4xl mx-auto mb-10">
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1 relative">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <Search className="h-5 w-5 text-gray-400" />
              </div>
              <input
                type="text"
                placeholder="Search by author, book, or poem title..."
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:ring-tamil-blue focus:border-tamil-blue"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
            
            <div className="md:w-48">
              <select
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-tamil-blue focus:border-tamil-blue"
                value={filterAuthor}
                onChange={(e) => setFilterAuthor(e.target.value)}
              >
                <option value="">All Authors</option>
                {authors.map(author => (
                  <option key={author} value={author}>{author}</option>
                ))}
              </select>
            </div>
          </div>
        </div>
        
        {/* Poems Display */}
        <div className="max-w-4xl mx-auto">
          {filteredPoems.length === 0 ? (
            <div className="text-center py-10">
              <p className="text-gray-500">No poems found matching your search criteria.</p>
            </div>
          ) : (
            filteredPoems.map((author) => (
              <div key={author.author} className="mb-12">
                <h2 className="text-2xl font-bold mb-6 text-tamil-blue-dark">{author.author}</h2>
                
                {author.books.map((book) => (
                  <div key={book.booktitle} className="mb-8">
                    <h3 className="text-xl font-semibold mb-4 pl-4 border-l-4 border-tamil-gold">
                      {book.booktitle}
                      {book.category && <span className="text-sm text-gray-500 ml-2">({book.category})</span>}
                    </h3>
                    
                    {book.description && (
                      <p className="text-gray-600 mb-4 pl-4">{book.description}</p>
                    )}
                    
                    {book.context.map((poem) => (
                      <div key={poem.title} className="mb-8 poem-container">
                        <h4 className="text-lg font-semibold mb-3 tamil-text">{poem.title}</h4>
                        <div className="poem-line whitespace-pre-line mb-4">
                          {poem.line}
                        </div>
                        
                        {poem.meaning && (
                          <div className="mt-4 pt-4 border-t border-gray-200">
                            <h5 className="text-sm font-semibold text-gray-500 mb-2">Meaning / Translation:</h5>
                            <p className="text-gray-600">{poem.meaning}</p>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                ))}
              </div>
            ))
          )}
        </div>
        
        {/* Export JSON Button */}
        <div className="max-w-4xl mx-auto mt-8 text-center">
          <button 
            onClick={() => {
              const dataStr = JSON.stringify(poemsData, null, 2);
              const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
              const exportFileDefaultName = 'tamil-kavithaigal.json';
              
              const linkElement = document.createElement('a');
              linkElement.setAttribute('href', dataUri);
              linkElement.setAttribute('download', exportFileDefaultName);
              linkElement.click();
            }}
            className="btn-secondary"
          >
            Export as JSON
          </button>
        </div>
      </div>
    </div>
  );
};

export default PreviewPage;
