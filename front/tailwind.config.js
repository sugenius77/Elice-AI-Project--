module.exports = {
    content: ["./src/**/*.{js,jsx,ts,tsx}"],
    theme: {
        extend: {
            colors: {
                theme: "#9AA4AE",
                primary: "#2980b9",
                sub: "#e5e5e5",
                point: "#fca311",
                point2: "#14213d",
                fontcolor: "#32292F",
            },
            fontFamily: {
                doogle: ["Source Sans Pro", "sans-serif"],
            },
        },
        screens: {
            "3xl": { max: "2000px" },
            "2xl": { max: "1535px" },
            // => @media (max-width: 1535px) { ... }

            xl: { max: "1279px" },
            // => @media (max-width: 1279px) { ... }

            lg: { max: "1023px" },
            // => @media (max-width: 1023px) { ... }

            md: { max: "767px" },
            // => @media (max-width: 767px) { ... }

            sm: { max: "639px" },
            // => @media (max-width: 639px) { ... }
        },
    },
    plugins: [
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
    ],
};
