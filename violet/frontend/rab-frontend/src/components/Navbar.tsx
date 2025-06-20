import './Navbar.css'

const Navbar = () => {
    return (
        <div>
            <nav className='navbar'>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/">History</a></li>
                    <li><a href="/">Settings</a></li>  
                </ul>
            </nav>
        </div>

    );

};

export default Navbar;