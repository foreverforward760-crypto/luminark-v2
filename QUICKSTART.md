# Luminark v2.0 - Quick Start Guide

## 🚀 Get Running in 5 Minutes

### Step 1: Extract Files
You already have the files! You're reading this. ✓

### Step 2: Install Dependencies
```bash
cd luminark-app
npm install
```
⏱️ *Takes ~2 minutes*

### Step 3: Start Development Server
```bash
npm run dev
```

### Step 4: Open Browser
```
http://localhost:3000
```

**That's it!** 🎉 Your Luminark app is running.

---

## 🎯 What to Do First

### 1. Complete Your First Assessment
- Click "Begin Assessment"
- Choose past or future focus
- Select your life domains (try multiple!)
- Adjust the 5 vector sliders
- Write your journal entry
- Save and view results

### 2. Explore Features
- 📖 Click "Stage Index" to see all 10 stages
- 📊 Click "Progress" to view your dashboard
- ℹ️ Hover over "i" buttons for helpful tips
- 🎨 Notice the smooth animations

### 3. Track Your Journey
- Complete assessments weekly or monthly
- Watch your stage progression over time
- Review past journal entries
- Observe patterns in your vectors

---

## 📱 Key Features at a Glance

| Feature | Description |
|---------|-------------|
| **Multi-Domain Selection** | Choose multiple life focus areas |
| **Detailed Reflections** | Write comprehensive thoughts, not just keywords |
| **Progress Charts** | Visual timeline of your transformation |
| **Stage Index** | Complete reference guide to all stages |
| **Info Tooltips** | Contextual help throughout |
| **Journal System** | Track entries with timestamps |
| **Radar Chart** | See your vector distribution |
| **Dark Theme** | Beautiful purple/blue aesthetic |

---

## 🎨 The Assessment Process

### 1️⃣ Time Orientation (Step 1)
**Question:** Are you focused on past or future?
- **Past**: Processing, healing, understanding patterns
- **Future**: Building, planning, creating vision

**What to do:** Choose your focus, then write detailed reflection

### 2️⃣ Life Focus Areas (Step 2)
**Question:** Where is your energy concentrated?
- 21 domains across 5 categories
- Select **all that apply**
- Multiple selections capture complex life situations

**Categories:**
- 🏛️ Core Foundations (basics of daily life)
- ✨ Meaning & Purpose (depth and significance)
- 🦅 Freedom & Autonomy (independence and power)
- 🏘️ Belonging & Safety (connection and security)
- 🎭 Experience & Recovery (enjoyment and healing)

### 3️⃣ Vector Assessment (Step 3)
**Rate 5 dimensions of your current state:**

1. **System Complexity**: How many balls are you juggling?
2. **Foundational Stability**: How solid is your ground?
3. **Internal Tension**: How much pressure do you feel?
4. **Fluid Adaptability**: How easily can you change?
5. **Pattern Coherence**: How aligned are your actions with values?

**Watch your stage number update** as you move the sliders!

### 4️⃣ Journal Entry (Step 4)
**Reflect on your current state:**
- See your calculated stage (0-9)
- Read the stage description and guidance
- Write what's alive for you
- Choose weekly or monthly tracking
- Save your entry

---

## 🔢 Understanding Your Stage

Your stage (0-9) is calculated from your vector scores:

```
Average of 5 vectors → Normalized to 0-9 range → Your Stage
```

### The Journey

```
0 → PLENARA (The Void)          Pure potential
1 → PULSE (Emergence)           First stirring
2 → DUALITY (The Split)         Meeting the other
3 → EXPRESSION (The Spark)      Creative chaos
4 → FOUNDATION (The Square)     Building structure
5 → THRESHOLD (The Crisis)      Point of no return
6 → INTEGRATION (Flow)          Everything works
7 → DISSOLUTION (The Alchemy)   Deep purification
8 → UNITY PEAK (The Trap)       Maximum achievement
9 → RELEASE (Transparency)      Wisdom without attachment
```

**The cycle repeats.** Stage 9 leads back to Stage 0.

---

## 📊 Using the Progress Dashboard

### What You'll See

1. **Statistics Cards**
   - Total entries recorded
   - Average stage across all assessments
   - Recent stage change (↑↓)

2. **Stage Progression Chart**
   - Line graph of your journey
   - X-axis: Dates
   - Y-axis: Stage number (0-9)
   - See patterns: Are you cycling? Growing? Stable?

3. **Vector Radar Chart**
   - Current state visualization
   - 5 axes for 5 vectors
   - Visual balance indicator

4. **Journal Timeline**
   - Reverse chronological entries
   - Full context: domains, reflections, journal text
   - Click to expand

---

## 💡 Pro Tips

### For Better Insights
1. **Be honest with sliders** - There are no "good" or "bad" stages
2. **Journal regularly** - Weekly tracking shows patterns clearly
3. **Review past entries** - Notice what was true then vs now
4. **Use the Stage Index** - Read ahead to see what's coming
5. **Trust the process** - All stages are necessary

### For Best Experience
1. **Desktop recommended** for first assessment (charts display better)
2. **Mobile works great** for quick check-ins
3. **Bookmark the site** for easy access
4. **Don't clear browser data** (unless you want to reset)
5. **Export journal entries** (copy from browser console if needed)

### For Developers
1. **Edit colors** in `tailwind.config.js`
2. **Modify stage descriptions** in `data/systemData.ts`
3. **Add life domains** in `data/systemData.ts`
4. **Customize animations** in `globals.css`
5. **Deploy to Vercel** (see DEPLOYMENT.md)

---

## 🆘 Troubleshooting

### App won't start
```bash
rm -rf node_modules package-lock.json .next
npm install
npm run dev
```

### Can't see my journal entries
- Check browser: Are you in incognito mode?
- Try: `localStorage.getItem('luminark-journal')` in console
- Ensure you clicked "Save Entry & Complete"

### Sliders not working
- Refresh the page
- Try different browser
- Check browser console for errors

### Chart not displaying
- Ensure you have multiple entries
- Try desktop browser
- Check window width (responsive breakpoints)

---

## 🎓 Learning Resources

### Understanding the System
- Read the **Stage Index** (📖 button)
- Hover over **info buttons** (ℹ️) throughout
- Review **CHANGELOG.md** for feature details
- Check **README.md** for technical overview

### Going Deeper
- Complete multiple assessments to see patterns
- Journal after significant life events
- Compare entries from different stages
- Notice what triggers stage transitions

---

## 🌟 What Makes Luminark Special

### It's Not Just Another Assessment Tool

1. **Cyclical, Not Linear**: There's no "winning" - all stages are valuable
2. **Self-Compassionate**: Meets you where you are
3. **Comprehensive**: Captures complexity without oversimplifying
4. **Beautiful**: Interface that respects your journey
5. **Private**: Your data never leaves your device
6. **Free**: No subscriptions, no upsells, no tracking

### The Philosophy

> "You are not broken. You are in process."

Luminark recognizes that transformation is cyclical. You'll visit these stages many times in your life. Each visit teaches something new. There's no final destination—only the journey itself.

---

## 📞 Need Help?

### Quick Checks
- ✅ Node.js 18+ installed?
- ✅ Ran `npm install`?
- ✅ No error messages in terminal?
- ✅ Port 3000 available?

### Still Stuck?
1. Read the full **README.md**
2. Check **DEPLOYMENT.md** for deployment issues
3. Review **CHANGELOG.md** for known issues
4. Open browser console (F12) for error messages

---

## 🚀 Ready to Deploy?

Once you're happy with local testing:

1. **Push to GitHub** (see DEPLOYMENT.md)
2. **Deploy to Vercel** (3 clicks, 2 minutes)
3. **Share with others** (optional)
4. **Keep assessing** and watch your transformation unfold

---

**Welcome to your journey through the archetypal stages.** 🌟

The Antikythera Engine is ready. Begin when you are.
