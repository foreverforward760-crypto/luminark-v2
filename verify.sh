#!/bin/bash

# Luminark v2.0 - Installation Verification Script
# Run this after extracting the archive to verify everything is ready

echo "=================================="
echo "🌟 Luminark v2.0 Verification"
echo "=================================="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Node.js
echo -n "Checking Node.js version... "
if command -v node &> /dev/null; then
    NODE_VERSION=$(node -v)
    echo -e "${GREEN}✓ Found: $NODE_VERSION${NC}"
else
    echo -e "${RED}✗ Node.js not found${NC}"
    echo "Please install Node.js 18+ from https://nodejs.org"
    exit 1
fi

# Check npm
echo -n "Checking npm... "
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm -v)
    echo -e "${GREEN}✓ Found: v$NPM_VERSION${NC}"
else
    echo -e "${RED}✗ npm not found${NC}"
    exit 1
fi

echo ""
echo "Checking project files..."

# Check key files
FILES=(
    "package.json"
    "tsconfig.json"
    "tailwind.config.js"
    "next.config.js"
    "app/page.tsx"
    "app/layout.tsx"
    "components/InfoButton.tsx"
    "components/StageIndex.tsx"
    "components/ProgressDashboard.tsx"
    "data/systemData.ts"
)

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "  ${GREEN}✓${NC} $file"
    else
        echo -e "  ${RED}✗${NC} $file (missing)"
    fi
done

echo ""
echo "Checking documentation..."

DOCS=(
    "README.md"
    "QUICKSTART.md"
    "DEPLOYMENT.md"
    "CHANGELOG.md"
    "PROJECT-SUMMARY.md"
    "DESIGN-REPORT.md"
)

for doc in "${DOCS[@]}"; do
    if [ -f "$doc" ]; then
        echo -e "  ${GREEN}✓${NC} $doc"
    else
        echo -e "  ${YELLOW}⚠${NC} $doc (optional)"
    fi
done

echo ""
echo "=================================="
echo "📦 Installation Status"
echo "=================================="

if [ -d "node_modules" ]; then
    echo -e "${GREEN}✓ Dependencies installed${NC}"
    echo ""
    echo "Ready to run! Execute:"
    echo "  npm run dev"
else
    echo -e "${YELLOW}⚠ Dependencies not installed${NC}"
    echo ""
    echo "Next step: Install dependencies"
    echo "  npm install"
    echo ""
    echo "Then run:"
    echo "  npm run dev"
fi

echo ""
echo "=================================="
echo "📚 Quick Reference"
echo "=================================="
echo "  QUICKSTART.md   - Get running in 5 minutes"
echo "  README.md       - Complete overview"
echo "  DEPLOYMENT.md   - GitHub & Vercel guide"
echo ""
echo "Questions? Check the documentation!"
echo ""
