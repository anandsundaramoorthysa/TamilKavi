import React, { useState, useEffect } from 'react';
import { AlertCircle, Check, Loader2 } from 'lucide-react';

const SubmitPage = () => {
  useEffect(() => {
    document.title = 'Submit | TamilKavi';
    window.scrollTo(0, 0);
  }, []);
  const [formData, setFormData] = useState({
    authorName: '',
    bookName: '',
    poemTitle: '',
    poemText: '',
    poemMeaning: '',
    email: '',
    githubUsername: '',
    confirmOriginal: false
  });
  
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submissionStatus, setSubmissionStatus] = useState<'idle' | 'success' | 'error'>('idle');
  const [submitMessage, setSubmitMessage] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
    
    // Clear error when user types
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: ''
      });
    }
  };

  const handleCheckboxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, checked } = e.target;
    setFormData({
      ...formData,
      [name]: checked
    });
    
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: ''
      });
    }
  };

  const validateForm = () => {
    const newErrors: Record<string, string> = {};
    
    if (!formData.authorName.trim()) {
      newErrors.authorName = 'Author name is required';
    }
    
    if (!formData.poemTitle.trim()) {
      newErrors.poemTitle = 'Poem title is required';
    }
    
    if (!formData.poemText.trim()) {
      newErrors.poemText = 'Poem text is required';
    }
    
    if (!formData.confirmOriginal) {
      newErrors.confirmOriginal = 'Please confirm that you have the rights to submit this content';
    }
    
    if (formData.email && !/^\S+@\S+\.\S+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email address';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (validateForm()) {
      setIsSubmitting(true);
      
      // Simulate API call
      setTimeout(() => {
        setIsSubmitting(false);
        setSubmissionStatus('success');
        setSubmitMessage('Your poem has been submitted successfully! Our team will review it shortly.');
        
        // Reset form after submission
        setFormData({
          authorName: '',
          bookName: '',
          poemTitle: '',
          poemText: '',
          poemMeaning: '',
          email: '',
          githubUsername: '',
          confirmOriginal: false
        });
      }, 1500);
    }
  };

  return (
    <div className="py-12">
      <div className="container-custom">
        <h1 className="text-4xl font-bold text-center mb-6">Submit a Kavithai</h1>
        <p className="text-lg text-center mb-12 max-w-3xl mx-auto">
          Use this form to submit a Tamil poem to our collection. We welcome both original works and 
          classical poems that you'd like to see included in our database.
        </p>
        
        <div className="max-w-3xl mx-auto">
          {submissionStatus === 'success' ? (
            <div className="bg-green-50 border border-green-200 rounded-lg p-8 text-center">
              <div className="flex justify-center mb-4">
                <div className="bg-green-100 p-3 rounded-full">
                  <Check className="h-8 w-8 text-green-600" />
                </div>
              </div>
              <h3 className="text-xl font-bold mb-2 text-green-800">Submission Successful!</h3>
              <p className="text-green-700 mb-6">{submitMessage}</p>
              <button
                onClick={() => setSubmissionStatus('idle')}
                className="btn-primary"
              >
                Submit Another Poem
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-sm border border-gray-100 p-8">
              <div className="space-y-6">
                {/* Author Name */}
                <div>
                  <label htmlFor="authorName" className="block text-sm font-medium text-gray-700 mb-1">
                    Author Name <span className="text-tamil-red">*</span>
                  </label>
                  <input
                    type="text"
                    id="authorName"
                    name="authorName"
                    value={formData.authorName}
                    onChange={handleChange}
                    className={`w-full px-4 py-2 border rounded-md ${
                      errors.authorName ? 'border-tamil-red' : 'border-gray-300'
                    } focus:ring-tamil-blue focus:border-tamil-blue`}
                    placeholder="e.g. Bharathiyar"
                  />
                  {errors.authorName && (
                    <p className="text-tamil-red text-sm mt-1">{errors.authorName}</p>
                  )}
                </div>
                
                {/* Book Name */}
                <div>
                  <label htmlFor="bookName" className="block text-sm font-medium text-gray-700 mb-1">
                    Book Name <span className="text-gray-500 text-sm">(optional)</span>
                  </label>
                  <input
                    type="text"
                    id="bookName"
                    name="bookName"
                    value={formData.bookName}
                    onChange={handleChange}
                    className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-tamil-blue focus:border-tamil-blue"
                    placeholder="e.g. Kannan Pattu"
                  />
                </div>
                
                {/* Poem Title */}
                <div>
                  <label htmlFor="poemTitle" className="block text-sm font-medium text-gray-700 mb-1">
                    Kavithai Title <span className="text-tamil-red">*</span>
                  </label>
                  <input
                    type="text"
                    id="poemTitle"
                    name="poemTitle"
                    value={formData.poemTitle}
                    onChange={handleChange}
                    className={`w-full px-4 py-2 border rounded-md ${
                      errors.poemTitle ? 'border-tamil-red' : 'border-gray-300'
                    } focus:ring-tamil-blue focus:border-tamil-blue`}
                    placeholder="e.g. வாழ்க நிரந்தரம்"
                  />
                  {errors.poemTitle && (
                    <p className="text-tamil-red text-sm mt-1">{errors.poemTitle}</p>
                  )}
                </div>
                
                {/* Poem Text */}
                <div>
                  <label htmlFor="poemText" className="block text-sm font-medium text-gray-700 mb-1">
                    Kavithai Text <span className="text-tamil-red">*</span>
                  </label>
                  <textarea
                    id="poemText"
                    name="poemText"
                    value={formData.poemText}
                    onChange={handleChange}
                    rows={6}
                    className={`w-full px-4 py-2 border rounded-md ${
                      errors.poemText ? 'border-tamil-red' : 'border-gray-300'
                    } focus:ring-tamil-blue focus:border-tamil-blue`}
                    placeholder="Paste the kavithai text here..."
                  />
                  {errors.poemText && (
                    <p className="text-tamil-red text-sm mt-1">{errors.poemText}</p>
                  )}
                  <p className="text-gray-500 text-sm mt-1">
                    For line breaks, please use Enter/Return key.
                  </p>
                </div>
                
                {/* Poem Meaning/Translation */}
                <div>
                  <label htmlFor="poemMeaning" className="block text-sm font-medium text-gray-700 mb-1">
                    Meaning or Translation <span className="text-gray-500 text-sm">(optional)</span>
                  </label>
                  <textarea
                    id="poemMeaning"
                    name="poemMeaning"
                    value={formData.poemMeaning}
                    onChange={handleChange}
                    rows={4}
                    className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-tamil-blue focus:border-tamil-blue"
                    placeholder="If you'd like to provide a meaning or translation for the poem, enter it here..."
                  />
                </div>
                
                {/* Contact Information */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
                      Email <span className="text-gray-500 text-sm">(optional)</span>
                    </label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleChange}
                      className={`w-full px-4 py-2 border rounded-md ${
                        errors.email ? 'border-tamil-red' : 'border-gray-300'
                      } focus:ring-tamil-blue focus:border-tamil-blue`}
                      placeholder="your@email.com"
                    />
                    {errors.email && (
                      <p className="text-tamil-red text-sm mt-1">{errors.email}</p>
                    )}
                  </div>
                  
                  <div>
                    <label htmlFor="githubUsername" className="block text-sm font-medium text-gray-700 mb-1">
                      GitHub Username <span className="text-gray-500 text-sm">(optional)</span>
                    </label>
                    <input
                      type="text"
                      id="githubUsername"
                      name="githubUsername"
                      value={formData.githubUsername}
                      onChange={handleChange}
                      className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-tamil-blue focus:border-tamil-blue"
                      placeholder="e.g. username"
                    />
                  </div>
                </div>
                
                {/* Confirmation Checkbox */}
                <div className="mt-6">
                  <div className="flex items-start">
                    <div className="flex items-center h-5">
                      <input
                        id="confirmOriginal"
                        name="confirmOriginal"
                        type="checkbox"
                        checked={formData.confirmOriginal}
                        onChange={handleCheckboxChange}
                        className="h-4 w-4 text-tamil-blue focus:ring-tamil-blue border-gray-300 rounded"
                      />
                    </div>
                    <div className="ml-3 text-sm">
                      <label htmlFor="confirmOriginal" className={`font-medium ${errors.confirmOriginal ? 'text-tamil-red' : 'text-gray-700'}`}>
                        I confirm that I have the rights to submit this content
                      </label>
                      <p className="text-gray-500">
                        By checking this box, you confirm that you either wrote the poem yourself, 
                        or it's in the public domain, or you have permission to contribute it.
                      </p>
                    </div>
                  </div>
                  {errors.confirmOriginal && (
                    <p className="text-tamil-red text-sm mt-1">{errors.confirmOriginal}</p>
                  )}
                </div>
                
                {/* Warning Note */}
                <div className="bg-amber-50 p-4 rounded-md flex">
                  <AlertCircle className="h-5 w-5 text-amber-500 mr-3 flex-shrink-0 mt-0.5" />
                  <p className="text-amber-700 text-sm">
                    Please ensure you have the rights to submit this content. We respect copyright and 
                    intellectual property rights. Content found to violate these rights will be removed.
                  </p>
                </div>
                
                {/* Submit Button */}
                <div className="flex justify-center">
                  <button
                    type="submit"
                    disabled={isSubmitting}
                    className="btn-primary flex items-center"
                  >
                    {isSubmitting && <Loader2 className="h-5 w-5 mr-2 animate-spin" />}
                    {isSubmitting ? 'Submitting...' : 'Submit Kavithai'}
                  </button>
                </div>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};

export default SubmitPage;
