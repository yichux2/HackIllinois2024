import { writeFile } from 'fs/promises'
import { NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest){
  console.log('gotten');
  
  return NextResponse.json({ success: true })
}

export async function POST(request: NextRequest) {
  console.log('called');
  const data = await request.formData()
  const file: File | null = data.get('file') as unknown as File

  if (!file) {
    return NextResponse.json({ success: false })
  }

  const bytes = await file.arrayBuffer()
  const buffer = Buffer.from(bytes)

  // With the file data in the buffer, you can do whatever you want with it.
  // For this, we'll just write it to the filesystem in a new location
  const path = `../../files/${file.name}`
  await writeFile(path, buffer)
  console.log(`open ${path} to see the uploaded file`)

  return NextResponse.json({ success: true })
}