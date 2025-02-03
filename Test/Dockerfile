# Use official Node.js image as a base image
FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the app's source code
COPY . .

# Expose the port that the app will use
EXPOSE 3000

# Command to run the app
CMD ["npm", "start"]
