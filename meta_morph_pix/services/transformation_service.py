import io

from PIL import Image, ExifTags


async def transform_image(image):
    image_content = await image.read()
    with Image.open(io.BytesIO(image_content)) as img:
        img = correct_image_orientation(img)
        img = resize_image(img)
        return decrease_quality(img, 80)


def resize_image(image, width=1800, height=1200):
    """
    Resize an image to the specified width and height.

    Parameters:
    - image: Image object.
    - width: New width.
    - height: New height.

    Returns:
    - img: Resized image object.
    """
    image.thumbnail((width, height))
    return image


def correct_image_orientation(image):
    """
    Correct the orientation of an image based on its EXIF data.

    Parameters:
    - img_path: Path to the image.

    Returns:
    - img: Image object with corrected orientation.
    """
    # Check for EXIF data (metadata)
    exif = image._getexif()
    if exif is not None:
        # Check for orientation key
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        # Use the orientation key to get the orientation value
        if orientation in exif:
            orientation_value = exif[orientation]

            # Rotate the image according to the orientation value
            if orientation_value == 2:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation_value == 3:
                image = image.rotate(180)
            elif orientation_value == 4:
                image = image.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation_value == 5:
                image = image.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation_value == 6:
                image = image.rotate(-90, expand=True)
            elif orientation_value == 7:
                image = image.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation_value == 8:
                image = image.rotate(90, expand=True)

    return image


def decrease_quality(image, quality=100):
    """
    Decrease the quality of an image.

    Parameters:
    - image: Image object.
    - quality: New quality.

    Returns:
    - img: Image object with decreased quality.
    """
    buffer = io.BytesIO()
    # path = "/Users/yelopez/git/yesid/meta-morph-pix/assets"
    # image.save(f"{path}/transformed.jpg", "JPEG", quality=quality, optimize=True)
    image.save(buffer, "JPEG", quality=quality)
    buffer.seek(0)
    return buffer
