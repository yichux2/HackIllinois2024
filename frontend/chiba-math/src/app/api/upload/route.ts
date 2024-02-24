import { writeFile } from 'fs/promises'
import { NextRequest, NextResponse } from 'next/server'
import got from 'got';

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
  const path = `../../SimpleTex/SimpleTex_scripts/images/${file.name}`
  await writeFile(path, buffer)
  console.log(`open ${path} to see the uploaded file`)

  const simpletex = await got.get(`http://localhost:5000/get_SimpleTex/${file.name}`);
  const obj = JSON.parse(simpletex.body);
  console.log(obj.res.latex);
  // console.log(obj.res);
  // const str = simpletex.body.replaceAll("\\",'');

  // console.log(Object.keys(obj));
  console.log('before')
  const openaireq = await got.post(`http://localhost:5000/process`,{json:{"text":obj.res.latex}})
  console.log('after')
  console.log(openaireq.body)
  return NextResponse.json({ success: true, body: JSON.parse(openaireq.body)})
}