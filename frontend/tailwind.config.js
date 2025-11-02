/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./pages/**/*.{js,jsx}", "./components/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        gold:   '#D4AF37',
        bronze: '#CD7F32',
        ink:    '#0B0B0D',
      },
    },
  },
  plugins: [],
}
