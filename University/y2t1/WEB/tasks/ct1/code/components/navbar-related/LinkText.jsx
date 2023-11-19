import Link from "next/link";

const LinkText = ({ href, children, active }) => {
  return (
    <Link
      className={`duration-300 ${
        active ? "text-slate-100" : "hover:text-slate-200 active:text-slate-300"
      }`}
      href={href}
    >
      {children === "Shows" ? (children = "TV Shows") : children}
    </Link>
  );
};

export default LinkText;
