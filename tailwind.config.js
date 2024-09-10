/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
  ],
  theme: {
    extend: {
      
      backgroundImage: {
        'custom-image': "url('/static/image/bg.jpg')",
        'custom-image': "url('/static/image/login.jpg')"
    },},
  },
  plugins: [],
}

