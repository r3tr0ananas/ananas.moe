/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./md/**/*.md", "./blog/md/**/*.md"],
  theme: {
    extend: {
      fontFamily: {
        "playpen": ["Playpen Sans"],
      },
      colors: {
        ananas: {
          DEFAULT: "#ffcb00",
          100: "#ffde00",
          400: "#ffcb00",
          800: "#cca300"
        },
        aGrey: {
          DEFAULT: "#505050",
          100: "#606060",
          300: "#505050",
          500: "#404040",
          600: "#333333",
          800: "#282828"
        },
        aDark: {
          DEFAULT: "#0e1114",
          100: "#2e3741",
          500: "#191e23",
          800: "#0e1114"
        }
      },
      screens: {
        "mobile": {"max": "430px"},
        "tablet": {"max": "850px"},
        "desktop": {"max": "1280px"}
      },
    }
  },
}
