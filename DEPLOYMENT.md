# Luminark v2.0 - GitHub Deployment Guide

## Quick Start: Push to GitHub

### Step 1: Initialize Git Repository

```bash
cd luminark-app
git init
git add .
git commit -m "Initial commit: Luminark v2.0 with enhanced features"
```

### Step 2: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `luminark-app` (or your preferred name)
3. Description: "Luminark v2.0 - Personal transformation assessment system"
4. Choose Public or Private
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

### Step 3: Connect and Push

Replace `YOUR_USERNAME` with your GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/luminark-app.git
git branch -M main
git push -u origin main
```

## Deploy to Vercel (Recommended)

### Why Vercel?
- Optimized for Next.js
- Free tier with custom domains
- Automatic deployments on push
- Instant rollbacks
- Built-in analytics

### Deployment Steps

1. **Go to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Sign up/Login with GitHub

2. **Import Project**
   - Click "Add New..." → "Project"
   - Select your `luminark-app` repository
   - Click "Import"

3. **Configure Build Settings**
   - Framework Preset: **Next.js** (auto-detected)
   - Root Directory: `./`
   - Build Command: `npm run build` (auto-filled)
   - Output Directory: `.next` (auto-filled)
   - Install Command: `npm install` (auto-filled)

4. **Environment Variables**
   - None required for Luminark v2.0 (client-side only)

5. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app will be live at `luminark-app.vercel.app`

### Custom Domain (Optional)

1. Go to Project Settings → Domains
2. Add your custom domain
3. Configure DNS records as instructed
4. SSL certificate auto-generated

### Automatic Deployments

Every push to `main` branch will trigger automatic deployment:

```bash
git add .
git commit -m "Update: [your changes]"
git push
```

## Deploy to Netlify (Alternative)

### Deployment Steps

1. **Build Static Export**
   ```bash
   npm run build
   ```

2. **Install Netlify CLI**
   ```bash
   npm install -g netlify-cli
   ```

3. **Deploy**
   ```bash
   netlify deploy --prod
   ```

4. **Or Use Netlify UI**
   - Go to [netlify.com](https://netlify.com)
   - Drag and drop the `.next` folder

## Deploy to GitHub Pages (Static Export)

1. **Install gh-pages**
   ```bash
   npm install --save-dev gh-pages
   ```

2. **Update package.json**
   ```json
   {
     "scripts": {
       "deploy": "next build && next export && gh-pages -d out"
     }
   }
   ```

3. **Update next.config.js**
   ```javascript
   module.exports = {
     output: 'export',
     images: {
       unoptimized: true,
     },
   }
   ```

4. **Deploy**
   ```bash
   npm run deploy
   ```

## Post-Deployment Checklist

- [ ] Test all pages and features
- [ ] Verify responsive design on mobile
- [ ] Check browser console for errors
- [ ] Test journal entry creation
- [ ] Verify progress dashboard displays correctly
- [ ] Test localStorage persistence
- [ ] Verify Stage Index modal works
- [ ] Test all info tooltips

## Continuous Integration

### GitHub Actions (Optional)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Vercel

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm run build
      - uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID}}
          vercel-project-id: ${{ secrets.PROJECT_ID}}
```

## Update Workflow

### For Bug Fixes or Features

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes
# ... edit files ...

# Commit changes
git add .
git commit -m "Add: [feature description]"

# Push to GitHub
git push origin feature/your-feature-name

# Create Pull Request on GitHub
# Merge to main when ready
```

### For Quick Updates

```bash
# Make changes on main branch
git add .
git commit -m "Update: [what you changed]"
git push

# Automatic deployment will trigger
```

## Rollback Procedure

### On Vercel

1. Go to Deployments tab
2. Find previous working deployment
3. Click "..." → "Promote to Production"

### On Git

```bash
# Revert to previous commit
git revert HEAD
git push

# Or reset to specific commit
git reset --hard COMMIT_HASH
git push --force
```

## Troubleshooting

### Build Fails

1. Check Node.js version (18+ required)
2. Clear cache: `rm -rf .next node_modules package-lock.json`
3. Reinstall: `npm install`
4. Try local build: `npm run build`

### Deployment Success But Blank Page

1. Check browser console for errors
2. Verify `next.config.js` settings
3. Check Vercel build logs
4. Ensure all imports are correct

### LocalStorage Not Working

1. Check browser privacy settings
2. Ensure site uses HTTPS
3. Verify no incognito/private browsing

## Maintenance

### Regular Updates

```bash
# Update dependencies
npm update

# Check for vulnerabilities
npm audit

# Fix vulnerabilities
npm audit fix
```

### Backup Journal Data

Users can export their localStorage data:

```javascript
// In browser console
copy(localStorage.getItem('luminark-journal'))
```

## Support

For deployment issues:
- Check [Next.js deployment docs](https://nextjs.org/docs/deployment)
- Vercel support: [vercel.com/support](https://vercel.com/support)
- GitHub issues: Open issue in your repository

---

**Your Luminark app is now ready to transform lives!** ✨
