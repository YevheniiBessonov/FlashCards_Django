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
            },
            backgroundImage: {
                'custom-gradient-before': 'linear-gradient(to right, rgba(0, 255, 255, 1), rgba(255, 0, 150, 0.2))',
                'custom-gradient-after': 'linear-gradient(to right, rgba(0, 255, 255, 1), rgba(23, 37, 84, 1))',
                'dark-theme-background': 'linear-gradient(to bottom right, rgba(0, 100, 100, 1), rgba(100, 0, 60, 1))',
            },
            colors: {
                'customGradient': 'linear-gradient(to right, rgba(0, 255, 255, 1), rgba(23, 37, 84, 1))',
                'cyanColor': 'rgba(0, 255, 255, 1)',
                'pinkTransparentColor': 'rgba(255, 0, 150, 0.2)',
                'darkCyanColor': 'rgba(23, 37, 84, 1)',
            },
        },
    },
    plugins: [],

}