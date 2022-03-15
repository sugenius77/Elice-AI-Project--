module.exports = {
    content: ["./src/**/*.{js,jsx,ts,tsx}"],
    theme: {
        extend: {
            colors: {
                theme: "#2a5454",
                primary: "#ffffff",
                sub: "#F9E4C8",
                point: "#F9CF93",
                point2: "#fc475f",
                fontcolor: "#BFADA3",
                headerColor: "#4C4C42",
            },
            backgroundImage: {
                hero: "url('https://images.unsplash.com/photo-1601907560526-d679c8ed95ce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80')",
            },
            fontFamily: {
                notoSans: ["Noto Sans KR", "sans-serif"],
                // reviewsFont: ["Sunflower", "sans-serif"],
                title: ["Do Hyeon", "sans-serif"],
                subTitle: ["Nanum Gothic Coding", "monospace"],
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
        require("daisyui"),
        require("tailwindcss-textshadow"),
    ],
};
