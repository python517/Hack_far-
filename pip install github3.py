mkdir bhptrojan            # Create the main project directory
cd bhptrojan               # Navigate to the newly created directory
git init                   # Initialize a new Git repository
mkdir modules              # Create a directory for modules
mkdir config               # Create a directory for configuration
mkdir data                 # Create a directory for data
touch .gitignore           # Create a .gitignore file

git add .                  # Add all files to Git
git commit -m "Adds repo structure for trojan."   # Commit changes to Git

# Replace <yourusername> with your GitHub username
git remote add origin https://github.com/<yourusername>/bhptrojan.git   # Link the local repository to your GitHub repository

git push origin master      # Push changes to GitHub
