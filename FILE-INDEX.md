# 📂 Luminark v2.0 - File Index

## 🚀 Start Here

**First time?** Read in this order:
1. **PROJECT-SUMMARY.md** ← Overview of everything
2. **QUICKSTART.md** ← Get running in 5 minutes
3. **README.md** ← Technical details

**Ready to deploy?**
4. **DEPLOYMENT.md** ← GitHub & Vercel guide

**Want to verify?**
5. Run `./verify.sh` ← Checks your setup

---

## 📁 Complete File Structure

```
luminark-app/
│
├── 📚 DOCUMENTATION (Read These First!)
│   ├── PROJECT-SUMMARY.md      ⭐ START HERE - Complete overview
│   ├── QUICKSTART.md           ⭐ 5-minute setup guide
│   ├── README.md               ⭐ Technical documentation
│   ├── DEPLOYMENT.md           🚀 GitHub & deployment guide
│   ├── CHANGELOG.md            📝 Version history
│   ├── DESIGN-REPORT.md        🎨 Design preservation report
│   └── FILE-INDEX.md           📂 This file
│
├── 🛠️ SETUP & CONFIG
│   ├── package.json            📦 Dependencies & scripts
│   ├── tsconfig.json           ⚙️ TypeScript configuration
│   ├── tailwind.config.js      🎨 Styling configuration
│   ├── postcss.config.js       🎨 CSS processing
│   ├── next.config.js          ⚙️ Next.js configuration
│   ├── .gitignore              🚫 Git ignore rules
│   └── verify.sh               ✓ Installation checker
│
├── 📱 APPLICATION CODE
│   ├── app/
│   │   ├── layout.tsx          🏗️ Root layout & metadata
│   │   ├── page.tsx            🎯 Main app (674 lines)
│   │   └── globals.css         🎨 Global styles & animations
│   │
│   ├── components/
│   │   ├── InfoButton.tsx      ℹ️ Tooltip component
│   │   ├── StageIndex.tsx      📖 Stage reference modal
│   │   └── ProgressDashboard.tsx 📊 Charts & timeline
│   │
│   └── data/
│       └── systemData.ts       📚 All content (427 lines)
│           ├── 10 Archetypal Stages
│           ├── 21 Life Domains
│           └── 5 Assessment Vectors
│
└── 📦 GENERATED (After npm install)
    ├── node_modules/           📦 Dependencies (~300MB)
    ├── .next/                  🏗️ Build output
    └── package-lock.json       🔒 Dependency lock file
```

---

## 📖 Documentation Guide

### For Different Needs

#### "I want to start quickly"
→ **QUICKSTART.md** (7,647 chars)
- 3-command setup
- 5-minute walkthrough
- Feature highlights
- Troubleshooting

#### "I need complete information"
→ **README.md** (7,945 chars)
- Full feature list
- Technical stack
- Project structure
- Customization guide
- Data privacy info

#### "I want to understand everything"
→ **PROJECT-SUMMARY.md** (12,024 chars)
- Complete overview
- All requirements ✓
- Technical specs
- Design decisions
- Next steps

#### "I want to deploy to GitHub"
→ **DEPLOYMENT.md** (5,673 chars)
- GitHub setup steps
- Vercel deployment
- Alternative hosts
- Update workflow
- Troubleshooting

#### "What changed from v1?"
→ **CHANGELOG.md** (6,207 chars)
- New features
- Improvements
- Technical changes
- Future roadmap

#### "Was the design preserved?"
→ **DESIGN-REPORT.md** (9,689 chars)
- Visual fidelity check
- Before/after comparison
- Color & animation analysis
- Quality assurance

**Total Documentation:** 49,185 characters!

---

## 🗂️ File Details

### Source Files (TSX/TS)

| File | Lines | Purpose |
|------|-------|---------|
| `app/page.tsx` | 674 | Main application logic |
| `data/systemData.ts` | 427 | All stage/domain/vector content |
| `components/ProgressDashboard.tsx` | 242 | Charts and timeline |
| `components/StageIndex.tsx` | 79 | Stage reference modal |
| `app/layout.tsx` | 17 | Root layout |
| `components/InfoButton.tsx` | 30 | Tooltip component |
| `app/globals.css` | 95 | Global styles |

**Total Code:** ~1,564 lines

### Configuration Files

| File | Purpose |
|------|---------|
| `package.json` | Dependencies and scripts |
| `tsconfig.json` | TypeScript compiler options |
| `tailwind.config.js` | Tailwind CSS theme |
| `next.config.js` | Next.js settings |
| `postcss.config.js` | CSS processing |
| `.gitignore` | Git ignore patterns |

### Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| Development | `npm run dev` | Start dev server |
| Build | `npm run build` | Build for production |
| Start | `npm start` | Run production build |
| Verify | `./verify.sh` | Check installation |

---

## 🎯 Key Components Explained

### `app/page.tsx` (Main App)
**What it does:**
- Multi-step assessment flow
- State management
- LocalStorage persistence
- Stage calculation
- Journal entry handling

**Key features:**
- 5-step wizard (welcome → temporal → domains → assessment → journal)
- Real-time stage calculation
- Modal management
- Responsive design

### `components/ProgressDashboard.tsx`
**What it does:**
- Displays journal entries
- Renders charts
- Shows statistics
- Timeline view

**Includes:**
- Line chart (Recharts)
- Radar chart (Recharts)
- Entry cards
- Date formatting

### `components/StageIndex.tsx`
**What it does:**
- Stage reference modal
- Complete stage descriptions
- Guidance for each stage

**Content:**
- All 10 stages
- Full descriptions
- Specific guidance
- Smooth scrolling

### `components/InfoButton.tsx`
**What it does:**
- Reusable tooltip component
- Hover-to-reveal info
- Styled popover

**Used for:**
- Vector explanations
- Domain descriptions
- Context throughout app

### `data/systemData.ts`
**What it contains:**
- 10 archetypal stages (full descriptions)
- 21 life domains (across 5 categories)
- 5 assessment vectors (with guidance)

**Structure:**
```typescript
export const ARCHETYPAL_STAGES = [...]
export const LIFE_VECTORS = [...]
export const ASSESSMENT_VECTORS = [...]
```

---

## 📦 Dependencies

### Core Framework
```json
"next": "14.0.4"           // React framework
"react": "18.2.0"          // UI library
"react-dom": "18.2.0"      // DOM rendering
"typescript": "5.3.3"      // Type safety
```

### UI & Styling
```json
"tailwindcss": "3.4.0"     // Utility CSS
"framer-motion": "10.16.16" // Animations
```

### Charts & Utilities
```json
"recharts": "2.10.3"       // Charts
"date-fns": "3.0.6"        // Date formatting
```

**Total:** 6 runtime dependencies + dev dependencies

---

## 🎨 Customization Points

### Easy to Modify

**Colors** → `tailwind.config.js`
```javascript
colors: {
  luminark: {
    bg: '#0a0a0f',      // Change background
    accent: '#4a4aff',  // Change accent
    // ...
  }
}
```

**Stage Content** → `data/systemData.ts`
```typescript
{
  id: 0,
  name: "PLENARA",
  description: "...",  // Edit description
  fullDescription: "...", // Edit full text
  guidance: "..."     // Edit guidance
}
```

**Life Domains** → `data/systemData.ts`
```typescript
{
  category: "Core Foundations",
  domains: [
    { name: "...", description: "..." } // Add/edit domains
  ]
}
```

**Animations** → `app/globals.css`
```css
@keyframes fadeIn {
  /* Modify timing or effects */
}
```

---

## 🔍 Data Flow

### Assessment Journey
```
1. User selects temporal focus
   ↓
2. User writes reflection
   ↓
3. User selects multiple domains
   ↓
4. User adjusts 5 vector sliders
   ↓ (real-time calculation)
5. Stage number updates
   ↓
6. User writes journal entry
   ↓
7. Save to localStorage
   ↓
8. Display in Progress Dashboard
```

### LocalStorage Structure
```json
{
  "luminark-journal": [
    {
      "id": "timestamp",
      "date": "ISO date string",
      "stage": 0-9,
      "vectors": {
        "complexity": 0-10,
        "stability": 0-10,
        "tension": 0-10,
        "adaptability": 0-10,
        "coherence": 0-10
      },
      "reflections": {
        "pastReflection": "text",
        "futureVision": "text"
      },
      "selectedDomains": ["id1", "id2"],
      "journalText": "text"
    }
  ]
}
```

---

## 🚀 Getting Started Checklist

### Pre-Installation
- [ ] Node.js 18+ installed
- [ ] npm available
- [ ] Terminal/command line access
- [ ] Text editor ready (VS Code recommended)

### Installation
- [ ] Extract archive
- [ ] Navigate to folder
- [ ] Run `./verify.sh` (optional)
- [ ] Run `npm install`
- [ ] Run `npm run dev`
- [ ] Open http://localhost:3000

### First Use
- [ ] Complete a test assessment
- [ ] Check Stage Index
- [ ] View Progress Dashboard
- [ ] Test info tooltips
- [ ] Try mobile view

### Deployment
- [ ] Read DEPLOYMENT.md
- [ ] Create GitHub repo
- [ ] Push code
- [ ] Connect to Vercel
- [ ] Deploy!

---

## 💡 Pro Tips

### Development
```bash
# Clean rebuild
rm -rf .next node_modules
npm install
npm run dev

# Check for updates
npm outdated

# Build for production
npm run build
```

### Customization
1. Start with `data/systemData.ts` (content)
2. Then `tailwind.config.js` (colors)
3. Then component files (layout/behavior)

### Debugging
1. Check browser console (F12)
2. Check terminal for build errors
3. Verify localStorage in DevTools
4. Test in incognito mode (clean state)

---

## 🎓 Learning Path

### If you're new to Next.js
1. Complete the app as-is
2. Read `app/page.tsx` comments
3. Modify stage descriptions
4. Change colors
5. Add a new life domain

### If you're experienced
1. Review architecture
2. Extend with new features
3. Add backend integration
4. Implement Deep Agent AI
5. Create export features

---

## 📞 Support Resources

### Documentation (Offline)
- All 6 markdown files in this archive
- Inline code comments
- TypeScript types

### Online Resources
- Next.js: https://nextjs.org/docs
- React: https://react.dev
- Tailwind: https://tailwindcss.com/docs
- Framer Motion: https://www.framer.com/motion

### Questions?
- Check QUICKSTART.md first
- Then README.md for technical details
- Then DEPLOYMENT.md for deploy issues

---

## 🎉 Ready to Begin!

You have everything you need:
- ✅ Complete source code
- ✅ Comprehensive documentation
- ✅ Setup verification script
- ✅ Deployment guides
- ✅ Design reports

**Next Step:** Read **QUICKSTART.md** and get running! 🚀

---

**Luminark v2.0 - Built with intention. Ready for transformation.**

*This file: FILE-INDEX.md*
*Project: Luminark v2.0*
*Date: January 2026*
