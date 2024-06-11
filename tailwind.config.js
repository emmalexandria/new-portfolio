/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        'display': ["Roboto Slab Variable", "ui-serif"],
        'body': ["Montserrat Variable", "ui-sans-serif"],
      },
      colors: {

        'mono': {
          50: '#F8F8F8',
  100: '#EBEBEB',
  200: '#D1D1D1',
  300: '#B8B8B8',
  400: '#9E9E9E',
  500: '#858585',
  600: '#6B6B6B',
  700: '#525252',
  800: '#383838',
  900: '#1F1F1F',
  950: '#121212'
        },


        'primary': {
          '50': '#fef7ee',
          '100': '#feedd6',
          '200': '#fcd6ac',
          '300': '#f9b978',
          '400': '#f69141',
          '500': '#f3721c',
          '600': '#ec5b13',
          '700': '#bd4111',
          '800': '#963516',
          '900': '#792d15',
          '950': '#411409',
        },
      }
    },
  },
  plugins: [],
}

