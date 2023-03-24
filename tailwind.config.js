/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      backgroundImage: {
        'wallpaper': "url('../Wallpaper.jpg')",
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
  darkMode: 'media',
}
