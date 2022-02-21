import React from "react";
import Footer from "components/Footer";

const Layout = ({ children }) => {
    return (
        <div>
            <div className="content overflow-x-hidden">{children}</div>
            <Footer />
        </div>
    );
};

export default Layout;
