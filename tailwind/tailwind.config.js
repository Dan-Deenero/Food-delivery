/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../project/**/*.{html,py}",
    "../restaurant/**/*.{html,py}",
    "../account/**/*.{html,py}",
    "../templates/**/*.{html,py}",
    'node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {
      fontFamily: {
        custom: ['Nunito', 'sans-serif'],
        Popins: ['Poppins', 'sans-serif'],
      },
    },
  },
  plugins: [
    require("daisyui"),
    require('preline/plugin')
  ],
}

