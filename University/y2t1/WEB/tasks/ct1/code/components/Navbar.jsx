"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import LinkText from "./navbar/LinkText";
import LinkButton from "./navbar/LinkButton";

const Navbar = () => {
  const pathname = usePathname();

  const links = [
    { href: "/", label: "Home" },
    { href: "/catalog", label: "Catalog" },
    { href: "/movies", label: "Movies" },
    { href: "/shows", label: "Shows" },
  ];

  return (
    <>
      <nav className="bg-neutral-800 text-neutral-300 z-50 fixed bottom-0 left-0 right-0 md:sticky md:top-0">
        <div className="flex items-center justify-between p-2 gap-2 md:hidden">
          {links.map((link) => {
            const isActive = pathname === link.href;

            return (
              <LinkButton key={link.href} href={link.href} active={isActive}>
                {link.label}
              </LinkButton>
            );
          })}
        </div>
        <div className="hidden md:flex max-w-6xl mx-auto justify-between items-center p-4">
          <Link
            href={"/"}
            className="font-medium text-xl duration-300 text-white hover:text-indigo-400 active:text-indigo-300"
          >
            Flickster
          </Link>
          <div className="flex items-center justify-center gap-4">
            {links.map((link) => {
              const isActive = pathname === link.href;

              return (
                <LinkText key={link.href} href={link.href} active={isActive}>
                  {link.label}
                </LinkText>
              );
            })}
          </div>
          <input
            type="text"
            className="bg-inherit rounded-md border-2 p-1 px-4 border-neutral-700 hover:border-indigo-500 max-w-[16rem] focus:outline-none focus:border-indigo-600"
            placeholder="Search..."
          />
        </div>
      </nav>
    </>
  );
};

export default Navbar;
