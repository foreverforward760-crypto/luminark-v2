# Luminark v2.0 - System Assessment Application

![Luminark](https://img.shields.io/badge/version-2.0.0-blue)
![Next.js](https://img.shields.io/badge/Next.js-14.0-black)
![TypeScript](https://img.shields.io/badge/TypeScript-5.3-blue)

**The Antikythera Engine for Self-Understanding**

Luminark is a sophisticated self-assessment application that helps users understand their current position within 10 archetypal stages of personal transformation through a bio-rhythmic vector analysis system.

## ✨ Features

### Core Assessment System
- **5 Vector Analysis**: Complexity, Stability, Tension, Adaptability, Coherence
- **10 Archetypal Stages**: From Plenara (The Void) to Release (Transparency)
- **Time Orientation**: Past-focused vs Future-focused assessment calibration
- **Multi-Domain Selection**: Choose multiple life focus areas simultaneously
- **Comprehensive Stage Descriptions**: Detailed guidance for each stage

### Enhanced User Experience
- **Interactive Info Tooltips**: Contextual information throughout the app
- **Stage Index Reference**: Complete guide to all 10 archetypal stages
- **Detailed Reflections**: Expanded text fields for deeper personal insights
- **Smooth Animations**: Framer Motion powered transitions

### Journal & Progress Tracking
- **Weekly/Monthly Journaling**: Track your journey through the stages
- **Progress Dashboard**: Visual charts showing stage progression over time
- **Vector Radar Chart**: Current assessment displayed in radar format
- **Timeline View**: Historical journal entries with full context
- **LocalStorage Persistence**: All data saved locally in your browser

### Visual Design
- **Dark Theme**: Sophisticated gradient backgrounds
- **Luminark Color Palette**: Purple/blue accent colors
- **Responsive Layout**: Works on mobile, tablet, and desktop
- **Custom Slider Styling**: Beautiful range inputs with glow effects
- **Smooth Scrolling**: Custom scrollbar design

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ installed
- npm or yarn package manager

### Installation

1. **Clone or download the project**
```bash
cd luminark-app
```

2. **Install dependencies**
```bash
npm install
```

3. **Run development server**
```bash
npm run dev
```

4. **Open in browser**
```
http://localhost:3000
```

### Build for Production

```bash
npm run build
npm start
```

## 📁 Project Structure

```
luminark-app/
├── app/
│   ├── layout.tsx          # Root layout with metadata
│   ├── page.tsx             # Main application component
│   └── globals.css          # Global styles and animations
├── components/
│   ├── InfoButton.tsx       # Tooltip component for contextual help
│   ├── StageIndex.tsx       # Modal with full stage descriptions
│   └── ProgressDashboard.tsx # Charts and journal timeline
├── data/
│   └── systemData.ts        # All stage, vector, and domain data
├── package.json
├── tsconfig.json
├── tailwind.config.js
├── postcss.config.js
├── next.config.js
└── README.md
```

## 🎨 Key Components

### Main Assessment Flow

1. **Welcome Screen**: Introduction to the system
2. **Time Orientation**: Past vs Future focus with detailed reflection
3. **Life Focus Areas**: Multi-select domains across 5 categories
4. **Vector Assessment**: 5 slider-based assessments with real-time stage calculation
5. **Journal Entry**: Weekly/monthly journaling with current stage context
6. **Completion**: Summary and access to progress dashboard

### Data Models

#### Journal Entry
```typescript
interface JournalEntry {
  id: string;
  date: Date;
  stage: number;              // 0-9
  vectors: Record<string, number>;
  reflections: {
    pastReflection: string;
    futureVision: string;
  };
  selectedDomains: string[];
  journalText: string;
}
```

## 🎯 Assessment Methodology

### The 5 Vectors

1. **System Complexity (C)**: Number of variables and interdependencies
2. **Foundational Stability (S)**: Structural integrity and predictability
3. **Internal Tension (T)**: Pressure for change (potential energy)
4. **Fluid Adaptability (A)**: Capacity to change without collapse
5. **Pattern Coherence (H)**: Alignment of actions with values

### Stage Calculation

The current stage (0-9) is calculated by:
1. Averaging all 5 vector scores
2. Normalizing to 0-9 range
3. Rounding to nearest integer stage

### The 10 Archetypal Stages

- **Stage 0 - Plenara**: Pure potential before form
- **Stage 1 - Pulse**: First stirring of energy
- **Stage 2 - Duality**: Encountering the other
- **Stage 3 - Expression**: Creative breakthrough
- **Stage 4 - Foundation**: Building structure
- **Stage 5 - Threshold**: The crisis point
- **Stage 6 - Integration**: High performance flow
- **Stage 7 - Dissolution**: Deep purification
- **Stage 8 - Unity Peak**: Maximum achievement (The Trap)
- **Stage 9 - Release**: Wisdom and letting go

## 📊 Progress Tracking Features

### Visual Charts
- **Line Chart**: Stage progression over time
- **Radar Chart**: Current vector distribution
- **Statistics**: Total entries, average stage, recent changes

### Journal Timeline
- Chronological display of all entries
- Full context preservation (domains, reflections, journal text)
- Date formatting and categorization

## 🎨 Customization

### Color Scheme
Edit `tailwind.config.js` to modify the Luminark color palette:

```javascript
colors: {
  luminark: {
    bg: '#0a0a0f',
    card: '#15151f',
    border: '#2a2a3f',
    accent: '#4a4aff',
    text: '#e0e0ff',
    muted: '#8080a0',
  },
}
```

### Stage Descriptions
Modify `/data/systemData.ts` to customize stage descriptions, guidance, or add new stages.

### Life Domains
Add or modify life domain categories in `/data/systemData.ts` under `LIFE_VECTORS`.

## 🔒 Data Privacy

- **All data stored locally**: No server communication
- **LocalStorage only**: Data never leaves your browser
- **User-controlled**: Clear browser data to reset completely
- **No tracking**: No analytics or external services

## 📱 Responsive Design

- **Mobile-first**: Optimized for touch interfaces
- **Tablet support**: Adjusted layouts for medium screens
- **Desktop enhanced**: Full-width charts and multi-column layouts

## 🚀 Deployment

### Deploy to Vercel (Recommended)

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial Luminark v2.0"
git remote add origin YOUR_REPO_URL
git push -u origin main
```

2. **Connect to Vercel**
- Go to [vercel.com](https://vercel.com)
- Import your GitHub repository
- Configure build settings (auto-detected for Next.js)
- Deploy

### Deploy to Netlify

1. **Build the static export**
```bash
npm run build
```

2. **Deploy the `.next` folder** to Netlify

### Environment Variables

No environment variables required - this is a client-side only application.

## 🛠️ Development

### Technologies Used
- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Framer Motion**: Animation library
- **Recharts**: Chart components
- **date-fns**: Date formatting

### Code Quality
- TypeScript strict mode enabled
- ESLint configured
- Component-based architecture
- Responsive design patterns

## 📝 Future Enhancement Ideas

- [ ] Export journal entries to PDF/Markdown
- [ ] Custom stage creation
- [ ] Multi-user support with authentication
- [ ] Cloud sync (optional)
- [ ] Deep Agent AI integration for personalized guidance
- [ ] Shareable assessment results
- [ ] Stage transition notifications
- [ ] Comparative analysis between entries

## 🤝 Contributing

This is a personal assessment tool. Feel free to fork and customize for your own use.

## 📄 License

MIT License - Feel free to use and modify for personal or commercial projects.

## 🙏 Acknowledgments

Based on the original Luminark system design with enhancements for deeper self-reflection and progress tracking.

---

**Built with intention. Transform with awareness.**

For questions or support, please open an issue on GitHub.
