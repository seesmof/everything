import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Flickster",
  description:
    "An app for movie enthusiasts that aims to streamline movie finding and picking process.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="min-h-screen bg-slate-900 text-slate-100">
          <Navbar />
          {children}
        </div>
      </body>
    </html>
  );
}
