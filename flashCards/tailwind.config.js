/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './**/templates/**/*.html',
        './**/*.py',
    ],
    darkMode: 'class',
    theme: {
        extend: {
            fontFamily: {
                sans: ['Roboto', 'sans-serif'],
                heading: ['Montserrat', 'sans-serif'],
            },
            backgroundImage: {
                'custom-gradient': 'linear-gradient(to right, rgba(165, 243, 252, 0.3), rgba(253, 164, 175, 0.5))',
            }
        },
    },
    plugins: [],

}