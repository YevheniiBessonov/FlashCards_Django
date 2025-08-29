/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './**/templates/**/*.html',
        './**/*.py',
        './static/src/**/*.{js,css,html}',
    ],
    darkMode: 'class',
    theme: {
        extend: {
            fontFamily: {
                sans: ['Roboto', 'sans-serif'],
                heading: ['Montserrat', 'sans-serif'],
                anton: ['Anton', 'sans-serif'],
                archivo: ['Archivo', 'sans-serif'],

            },
            backgroundImage: {
                'custom-bg': "url('/static/flashcards_app/images/bg.png')",
                'custom-gradient-before': 'linear-gradient(to right, rgba(0, 255, 255, 0.4), rgba(255, 0, 150, 0.2))',
                'custom-gradient-after': 'linear-gradient(to right, rgba(0, 255, 255, 0.3), rgba(23, 37, 84, 1))',
                'dark-theme-background': 'linear-gradient(to bottom right, rgba(0, 100, 100, 0.4), rgba(100, 0, 60, 1))',
            },
            colors: {
                'gradient-start': 'rgba(42, 10, 75, 0.3)',
                'gradient-mid': 'rgba(10, 47, 75, 0.2)',
                'gradient-end': 'rgba(10, 75, 75, 0.3)',
            },
        },
    },
    plugins: [],

}