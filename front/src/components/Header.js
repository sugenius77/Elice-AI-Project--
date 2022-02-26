import React from "react";
import { Link } from "react-scroll";

const Header = () => {
    const menuItems = [
        {
            title: "Home",
            key: "/",
            index: 1,
        },
        {
            title: "Search",
            key: "/Search",
            index: 2,
        },
        {
            title: "Login",
            key: "/callback",
            index: 3,
        },
    ];

    return (
        <div className="font-doogle text-white fixed top-0 left-0 right-0 w-full z-50">
            <div
                className={`flex justify-between bg-theme items-center p-2 shadow-lg `}
            >
                <div className="flex justify-between w-full">
                    <Link to="/" className="text-4xl font-semibold mb-2">
                        H O T E L S
                    </Link>
                </div>
                <div className="flex cursor-pointer">
                    {menuItems.map((item) => {
                        return (
                            <li className="list-none mx-2 p-1">
                                <Link
                                    to={item.index}
                                    spy={true}
                                    smooth={true}
                                    key={item.index}
                                >
                                    {item.title}
                                </Link>
                            </li>
                        );
                    })}
                </div>
            </div>
        </div>
    );
};

export default Header;
