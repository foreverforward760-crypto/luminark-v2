import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Luminark - Self-Reflection Prototype',
  description: 'Experimental self-reflection and journaling app using the author’s 0-9-0 framework. Not a validated assessment or diagnostic tool.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
