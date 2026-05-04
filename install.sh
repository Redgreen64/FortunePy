#!/bin/bash
## DUMMY INSTALLER TEMPLATE
## Use this as a base for your own hosted repo.

# --- CONFIGURATION ---
URL="https://raw.githubusercontent.com/DatOneStormyz/fortunepy/main/" # OR https://your_domain.com/path/to/fortunepyandpytypewriter/
HOSTER="Stormy" 
HasLoadingThing=1 # 0: verbose, 1: progress bar, 2: both

# --- VISUALS ---
if command -v figlet >/dev/null 2>&1; then
    figlet "FORTUNEPY"
else
    echo "================================================"
    echo "      FORTUNEPY AND PYTYPEWRITER INSTALLER      "
    echo "================================================"
fi

echo "-------------------------------------------------------"
echo "Written in bash by the module creator himself (Stormy)"
echo "Hosted by: $HOSTER"
echo "-------------------------------------------------------"

# --- DEPENDENCY CHECK ---
echo "Checking for the basics..."
for cmd in fortune python3 curl; do
    if ! command -v $cmd >/dev/null 2>&1; then
        echo "ERROR: $cmd not found. Go install it. I'm not doing it for you."
        exit 1
    fi
done

# --- CALCULATE GLOBAL PATH ---
# This finds your user-specific site-packages so you don't need sudo.
USER_SITE_PACKAGES=$(python3 -m site --user-site)

# Create the directory if it doesn't exist (it usually doesn't on fresh installs)
mkdir -p "$USER_SITE_PACKAGES"

# --- DOWNLOAD LOGIC ---
echo "Downloading FortunePy..."

if [ "$HasLoadingThing" -eq 1 ]; then
    curl -L "$URL" -o "fortunepy.py" --progress-bar
elif [ "$HasLoadingThing" -eq 0 ]; then
    curl -L "$URL" -o "fortunepy.py"
else
    echo "Fetching from $URL..."
    curl -L "$URL" -o "fortunepy.py" --progress-bar
fi

# --- THE AUTO-MOVE ---
if [ -f "fortunepy.py" ]; then
    echo "Installing to $USER_SITE_PACKAGES..."
    
    # Move the file so it can be imported from ANYWHERE
    mv fortunepy.py "$USER_SITE_PACKAGES/"

# --- DOWNLOAD LOGIC ---
echo "Downloading PyTypewriter..."

if [ "$HasLoadingThing" -eq 1 ]; then
    curl -L "$URL" -o "PyTypewriter.py" --progress-bar
elif [ "$HasLoadingThing" -eq 0 ]; then
    curl -L "$URL" -o "PyTypewriter.py"
else
    echo "Fetching from $URL..."
    curl -L "$URL" -o "PyTypewriter.py" --progress-bar
fi

# --- THE AUTO-MOVE ---
if [ -f "PyTypewriter.py" ]; then
    echo "Installing to $USER_SITE_PACKAGES..."
    
    # Move the file so it can be imported from ANYWHERE
    mv fortunepy.py "$USER_SITE_PACKAGES/"
    
    if [ $? -eq 0 ]; then
        echo "-------------------------------------------------------"
        echo "SUCCESS: FortunePy and PyTypewriter is now global."
        echo "You can now use 'import fortunepy' in any Python script."
        echo "-------------------------------------------------------"
        python3 -c "import fortunepy; print('Test: Installation verified.')"
    else
        echo "MOVE FAILED: Check your permissions. Maybe your system is locked down?"
    fi
else
    echo "DOWNLOAD FAILED: The file never arrived. Report this to the host or their fourms (if they have an Issues channel)."
    exit 1
fi
