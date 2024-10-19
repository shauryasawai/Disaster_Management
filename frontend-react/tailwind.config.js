// tailwind.config.js
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",  // This ensures Tailwind scans all React files
  ],
  theme: {
    extend: {
      animation: {
        'moving-border': 'move-border 2s linear infinite',
      },
      keyframes: {
        'move-border': {
          '0%': { backgroundPosition: '0% 50%' },
          '100%': { backgroundPosition: '100% 50%' },
        },
      },
    },
  },
  plugins: [],
};
