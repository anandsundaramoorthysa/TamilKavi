
export interface Poem {
  title: string;
  line: string;
  meaning?: string;
}

export interface Book {
  booktitle: string;
  coverimage?: string;
  description?: string;
  category?: string;
  context: Poem[];
}

export interface Author {
  author: string;
  contact?: string;
  books: Book[];
}

export const poemsData: Author[] = [
  {
    author: "Bharathiyar",
    contact: "",
    books: [
      {
        booktitle: "Desiya Kavithaigal",
        description: "Patriotic poems",
        category: "Patriotic",
        context: [
          {
            title: "வாழ்க நிரந்தரம்",
            line: "வாழ்க நிரந்தரம் வாழ்க தமிழ்மொழி\nவாழிய வாழியவே!\nஊழி தோறூழி உலகமுடனளாய்\nஓங்குக ஓங்குகவே!",
            meaning: "Long live Tamil language forever! May it flourish throughout the ages, spreading across the world!"
          }
        ]
      },
      {
        booktitle: "Kannan Pattu",
        description: "Poems about Lord Krishna",
        category: "Devotional",
        context: [
          {
            title: "சின்னஞ்சிறு கிளியே",
            line: "சின்னஞ்சிறு கிளியே கண்ணம்மா\nசெல்வக் கிளியே கண்ணம்மா\nஎந்தன் தமிழ்க்கிளியே கண்ணம்மா\nஇன்பக் கிளியே கண்ணம்மா",
            meaning: "My little parrot, my rich parrot, my Tamil parrot, my delightful parrot"
          }
        ]
      }
    ]
  },
  {
    author: "Kannadasan",
    contact: "",
    books: [
      {
        booktitle: "Arthamulla Indhu Matham",
        description: "Philosophical poems",
        category: "Philosophy",
        context: [
          {
            title: "கற்றவன் நாடு",
            line: "கற்றவன் நாடும் கரையற்ற கல்வி\nமற்றவன் நாடும் மதிப்பொன்றே",
            meaning: "The educated seek boundless knowledge; others seek only respect."
          }
        ]
      }
    ]
  },
  {
    author: "Vairamuthu",
    contact: "",
    books: [
      {
        booktitle: "Kallikkattu Ithikasam",
        description: "Epic poem about rural life",
        category: "Rural",
        context: [
          {
            title: "கள்ளிக்காட்டு இதிகாசம்",
            line: "உறவுகளைத் தேடிவரும் உலகத்தில்\nஉணவைத் தேடி வாழ்கின்றேன்.",
            meaning: "In a world that seeks relationships, I live seeking food."
          }
        ]
      }
    ]
  },
  {
    author: "Avvaiyar",
    contact: "",
    books: [
      {
        booktitle: "Aathichudi",
        description: "Moral teachings",
        category: "Ethics",
        context: [
          {
            title: "அறம் செய விரும்பு",
            line: "அறம் செய விரும்பு\nஆறுவது சினம்\nஇயல்வது கரவேல்\nஈவது விலக்கேல்",
            meaning: "Desire to do good. Control your anger. Don't hide your capabilities. Don't hold back from giving."
          }
        ]
      }
    ]
  }
];
