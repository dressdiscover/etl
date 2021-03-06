from .costume_core_predicate import CostumeCorePredicate
import rdflib.term

alternative = CostumeCorePredicate(
    description_text_en="Any additional titles by which the item is known, other than the preferred title, including nicknames or titles in other languages.",
    display_name_en="Alternative Title",
    id="alternative",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/alternative"),
    sub_property_of_uri=None,
    terms=None,
)
cataloguerWithDate = CostumeCorePredicate(
    description_text_en="Full names of all catalogers, with the date in parentheses, in the format YYYY-MM-DD.\n\nWhen additions are made to the catalog record, additional names and dates should be added and existing entries should not be deleted.",
    display_name_en="Cataloguer With Date",
    id="cataloguerWithDate",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/cataloguerWithDate"),
    sub_property_of_uri=None,
    terms=None,
)
cbLengthIn = CostumeCorePredicate(
    description_text_en="The center back measurement from top edge (neckline or waist) to hem, in inches, as decimals to the nearest quarter inch.",
    display_name_en="Center Back Length",
    id="cbLengthIn",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/cbLengthIn"),
    sub_property_of_uri=None,
    terms=None,
)
cfLengthIn = CostumeCorePredicate(
    description_text_en="The center front measurement from top edge (neckline or waist) to hem, in inches, as decimals to the nearest quarter inch.",
    display_name_en="Center Front Length",
    id="cfLengthIn",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/cfLengthIn"),
    sub_property_of_uri=None,
    terms=None,
)
chestIn = CostumeCorePredicate(
    description_text_en="The measurement straight around the fullest part of the chest, in inches, as decimals to the nearest quarter inch.",
    display_name_en="Chest",
    id="chestIn",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/chestIn"),
    sub_property_of_uri=None,
    terms=None,
)
classification = CostumeCorePredicate(
    description_text_en='A classification term should be applied for all costume items, such as "Costume," or "Fashion." This may vary based on the larger overall collection in which these objects will be published.',
    display_name_en="Classification",
    id="classification",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/classification"),
    sub_property_of_uri=None,
    terms=None,
)
closure = CostumeCorePredicate(
    description_text_en="Each closure used on the garment.",
    display_name_en="Closure",
    id="closure",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/closure"),
    sub_property_of_uri=None,
    terms=None,
)
closurePlacement = CostumeCorePredicate(
    description_text_en="Each placement of closures on the item.",
    display_name_en="Closure Placement",
    id="closurePlacement",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/closurePlacement"),
    sub_property_of_uri=None,
    terms=None,
)
collar = CostumeCorePredicate(
    description_text_en="Each term that describes the collar of the garment.",
    display_name_en="Collar",
    id="collar",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/collar"),
    sub_property_of_uri=None,
    terms=None,
)
colorMain = CostumeCorePredicate(
    description_text_en="The most dominant color in the garment.",
    display_name_en="Color Main",
    id="colorMain",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/colorMain"),
    sub_property_of_uri=None,
    terms=None,
)
colorSecondary = CostumeCorePredicate(
    description_text_en="Any additional colors in the garment.",
    display_name_en="Color Secondary",
    id="colorSecondary",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/colorSecondary"),
    sub_property_of_uri=None,
    terms=None,
)
condition = CostumeCorePredicate(
    description_text_en="A single term to indicate a rating of the overall condition of the object.",
    display_name_en="Condition Term",
    id="condition",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/condition"),
    sub_property_of_uri=None,
    terms=None,
)
conditionDescription = CostumeCorePredicate(
    description_text_en="Narrative description of the overall physical condition, characteristics, and completeness of a work, describing where each issue is located on the garment. \n\nThis may incorporate details checked off on a separate worksheet.",
    display_name_en="Condition Description",
    id="conditionDescription",
    _uri=rdflib.term.URIRef(
        "https://w3id.org/costumeCore/ontology/conditionDescription"
    ),
    sub_property_of_uri=None,
    terms=None,
)
costOriginal = CostumeCorePredicate(
    description_text_en="The cost of the object when originally created, indicating the units (dollars, etc.)",
    display_name_en="Cost Original",
    id="costOriginal",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/costOriginal"),
    sub_property_of_uri=None,
    terms=None,
)
costumeComponents = CostumeCorePredicate(
    description_text_en="Each additional component of the garment not included elsewhere.",
    display_name_en="Costume Components",
    id="costumeComponents",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/costumeComponents"),
    sub_property_of_uri=None,
    terms=None,
)
creator = CostumeCorePredicate(
    description_text_en="Full name of each known designer, maker, manufacturer, etc. \n\nUse the display form with first name first, not last name first.",
    display_name_en="Creator",
    id="creator",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/creator"),
    sub_property_of_uri=None,
    terms=None,
)
culturalContext = CostumeCorePredicate(
    description_text_en="The name(s) of the culture, people, or nationality from which the work originated or was used.\n",
    display_name_en="Culture",
    id="culturalContext",
    _uri=rdflib.term.URIRef("http://purl.org/vra/culturalContext"),
    sub_property_of_uri=None,
    terms=None,
)
date = CostumeCorePredicate(
    description_text_en='If known, the year in which the item was created. Otherwise, a range of years that it could possibly have been created, from the earliest to latest. A more precise date can be entered if known, as YYYY-MM or YYYY-MM-DD. Uncertainty can be indicated in parentheses after the date or range of dates (for example, "(circa)").\n\nFollow ISO 8601 standards for initial numbers and follow with additional display terms.',
    display_name_en="Date",
    id="date",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/date"),
    sub_property_of_uri=None,
    terms=None,
)
description = CostumeCorePredicate(
    description_text_en='Use the details from each component section of the data entry process to construct the full description for display. \n\nStart with one sentence that sums up the work type(s), colors, and important features. \n\nFollow with a description of materials and notable techniques, separated by commas. \n\nThe next sentences list each component with an ID number or letter in parentheses, ex. "bodice (a)", with structural details separated by commas (in order from the top down, outside in). This is the place to describe where particular materials or techniques are located on the garment.\n\nCopy from Description Autofill if available (as values) and edit as needed.',
    display_name_en="Description",
    id="description",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/description"),
    sub_property_of_uri=None,
    terms=None,
)
dimensionsOther = CostumeCorePredicate(
    description_text_en="Any other measurements that are notable on this garment, in inches, as decimals to the nearest quarter inch. Describe what the measurement is of, in parentheses, after the measurement.",
    display_name_en="Measurements Other",
    id="dimensionsOther",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/dimensionsOther"),
    sub_property_of_uri=None,
    terms=None,
)
donator = CostumeCorePredicate(
    description_text_en='Full name(s) of all donors. To protect the privacy of some private donors, they may request that this read simply "Anonymous" with no specifics. Instead, the specifics can be entered under "private information."',
    display_name_en="Donor",
    id="donator",
    _uri=rdflib.term.URIRef("http://purl.org/vra/donator"),
    sub_property_of_uri=None,
    terms=None,
)
dressType = CostumeCorePredicate(
    description_text_en="Each term that describes the type of dress.",
    display_name_en="Dress Type",
    id="dressType",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/dressType"),
    sub_property_of_uri=None,
    terms=None,
)
endDate = CostumeCorePredicate(
    description_text_en="The latest the garment could have been made, in the format YYYY or YYYY-MM or YYYY-MM-DD. Follow ISO 8601 standards.",
    display_name_en="Date Latest",
    id="endDate",
    _uri=rdflib.term.URIRef("http://purl.org/vra/endDate"),
    sub_property_of_uri=None,
    terms=None,
)
exhibitions = CostumeCorePredicate(
    description_text_en="A list of all exhibitions that included this object,  including the title or name of each exhibition, its location, and other pertinent information.",
    display_name_en="Exhibitions",
    id="exhibitions",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/exhibitions"),
    sub_property_of_uri=None,
    terms=None,
)
extent = CostumeCorePredicate(
    description_text_en="Use each separate measurement recorded in the data entry process to construct the full list of measurements for display.\n\nList all measurements of the item, separated by commas. Measurements should be in inches, to the nearest .25 inch. Describe the part being measured in parentheses.",
    display_name_en="Measurements Display",
    id="extent",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/extent"),
    sub_property_of_uri=None,
    terms=None,
)
fiber = CostumeCorePredicate(
    description_text_en="Each term for the type of fiber used in the materials of the object, distinguished from the textile type, trimmings, or other materials.",
    display_name_en="Fiber",
    id="fiber",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/fiber"),
    sub_property_of_uri=None,
    terms=None,
)
function = CostumeCorePredicate(
    description_text_en="Each function for which the object was worn. ",
    display_name_en="Function",
    id="function",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/function"),
    sub_property_of_uri=None,
    terms=None,
)
gender = CostumeCorePredicate(
    description_text_en="The gender for which the object was originally intended.",
    display_name_en="Gender",
    id="gender",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/gender"),
    sub_property_of_uri=None,
    terms=None,
)
hasInscription = CostumeCorePredicate(
    description_text_en="The exact text, in quotes, from each label within the object, followed by a phrase describing where the label is located on the object.",
    display_name_en="Label",
    id="hasInscription",
    _uri=rdflib.term.URIRef("http://purl.org/vra/hasInscription"),
    sub_property_of_uri=None,
    terms=None,
)
hasTechnique = CostumeCorePredicate(
    description_text_en="Each process involved in making the object. \n\nDo not include a description of where the technique is in evidence on the garment: that should be a part of the narrative description.",
    display_name_en="Technique",
    id="hasTechnique",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/hasTechnique"),
    sub_property_of_uri="http://purl.org/vra/hasTechnique",
    terms=None,
)
hemCircumferenceIn = CostumeCorePredicate(
    description_text_en="The measurement all around the hem, in inches, as decimals to the nearest quarter inch.",
    display_name_en="Hem Circumference",
    id="hemCircumferenceIn",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/hemCircumferenceIn"),
    sub_property_of_uri=None,
    terms=None,
)
hipsIn = CostumeCorePredicate(
    description_text_en="The measurement straight around the fullest part of the hips, in inches, as decimals to the nearest quarter inch.",
    display_name_en="Hips",
    id="hipsIn",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/hipsIn"),
    sub_property_of_uri=None,
    terms=None,
)
icomType = CostumeCorePredicate(
    description_text_en="The second and third level classes from the ICOM Vocabulary.",
    display_name_en="ICOM Type",
    id="icomType",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/icomType"),
    sub_property_of_uri=None,
    terms=None,
)
identifier = CostumeCorePredicate(
    description_text_en="A unique ID number for the item. This will often be formatted like VC1992124 (VC=repository, 1992 = year, 124 = serial number).\n\nNo spaces or uncommon characters.",
    display_name_en="Identifier",
    id="identifier",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/identifier"),
    sub_property_of_uri=None,
    terms=None,
)
isReferencedBy = CostumeCorePredicate(
    description_text_en="References about this object, or about similar objects in texts or online, as either a full bibliographic citation (in MLA format) or a URL.",
    display_name_en="References",
    id="isReferencedBy",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/isReferencedBy"),
    sub_property_of_uri=None,
    terms=None,
)
length = CostumeCorePredicate(
    description_text_en="Each length of the object, where the hem lands on the body.",
    display_name_en="Length",
    id="length",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/length"),
    sub_property_of_uri=None,
    terms=None,
)
lifeStages = CostumeCorePredicate(
    description_text_en="Each age of the wearer for which the object was intended.",
    display_name_en="Life Stages",
    id="lifeStages",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/lifeStages"),
    sub_property_of_uri=None,
    terms=None,
)
liturgicalType = CostumeCorePredicate(
    description_text_en="Each type of liturgical garment or accessory.",
    display_name_en="Liturgical Type",
    id="liturgicalType",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/liturgicalType"),
    sub_property_of_uri=None,
    terms=None,
)
mannequin = CostumeCorePredicate(
    description_text_en="The size and year, or name, of any mannequins the garment fits on for display.",
    display_name_en="Mannequin",
    id="mannequin",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/mannequin"),
    sub_property_of_uri=None,
    terms=None,
)
material = CostumeCorePredicate(
    description_text_en="Each material in the object.",
    display_name_en="Material",
    id="material",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/material"),
    sub_property_of_uri="http://purl.org/vra/material",
    terms=None,
)
neckline = CostumeCorePredicate(
    description_text_en="Each type of neckline of the garment.",
    display_name_en="Neckline",
    id="neckline",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/neckline"),
    sub_property_of_uri=None,
    terms=None,
)
otherMaterials = CostumeCorePredicate(
    description_text_en="Any other material terms that do not describe fibers, textiles, or trimmings.",
    display_name_en="Other Materials",
    id="otherMaterials",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/otherMaterials"),
    sub_property_of_uri=None,
    terms=None,
)
pantsType = CostumeCorePredicate(
    description_text_en="Each term that describes the length and shape of pants.",
    display_name_en="Pants Type",
    id="pantsType",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/pantsType"),
    sub_property_of_uri=None,
    terms=None,
)
pattern = CostumeCorePredicate(
    description_text_en="Each design motif appearing on the object.",
    display_name_en="Pattern",
    id="pattern",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/pattern"),
    sub_property_of_uri=None,
    terms=None,
)
placeOfRepository = CostumeCorePredicate(
    description_text_en="The name of the collection the garment belongs to, institutional or private. Include the address of a public institution, if appropriate. \n\nTo protect the privacy of some private collectors, they may request that this read simply 'Private Collection' with no specifics. Instead, the specifics can be entered under 'private information.'",
    display_name_en="Holding Institution",
    id="placeOfRepository",
    _uri=rdflib.term.URIRef("http://purl.org/vra/placeOfRepository"),
    sub_property_of_uri=None,
    terms=None,
)
privateInformation = CostumeCorePredicate(
    description_text_en="Any information that doesn't fit elsewhere, and isn't suited for public view (for example private stories or communication with the donor).",
    display_name_en="Private Information",
    id="privateInformation",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/privateInformation"),
    sub_property_of_uri=None,
    terms=None,
)
publicInformation = CostumeCorePredicate(
    description_text_en="A brief narrative about the object, with any interesting / important information (numbers in parentheses can provide links to external references, which then are also listed in reference field).\n\nInclude MLA style parenthetical citations to references listed in References field as needed.",
    display_name_en="Public Information",
    id="publicInformation",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/publicInformation"),
    sub_property_of_uri=None,
    terms=None,
)
relation = CostumeCorePredicate(
    description_text_en="Enter the identifier for any related items. For clothing artifacts this will be an ID# like VC1992124. For other relations, such as exhibitions, the identifier may take a different form, such as the title. See the identifier element in the item itself to check.",
    display_name_en="Relation",
    id="relation",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/relation"),
    sub_property_of_uri=None,
    terms=None,
)
rights = CostumeCorePredicate(
    description_text_en="A standardized rights statement. In most cases, clothing artifacts are not protected by copyright, but may be represented in images that are under copyright.",
    display_name_en="Rights",
    id="rights",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/rights"),
    sub_property_of_uri="http://purl.org/dc/terms/rights",
    terms=None,
)
rightsHolder = CostumeCorePredicate(
    description_text_en="A rights statement including what is covered (images or object itself), person or organization owning or managing rights, a copyright symbol and date if appropriate, and additional contact information. ",
    display_name_en="Rights Holder",
    id="rightsHolder",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/rightsHolder"),
    sub_property_of_uri=None,
    terms=None,
)
size = CostumeCorePredicate(
    description_text_en="The size of the object, if shown on a label or otherwise identified.",
    display_name_en="Size",
    id="size",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/size"),
    sub_property_of_uri=None,
    terms=None,
)
skirtType = CostumeCorePredicate(
    description_text_en="Each term that describes the skirt of the garment.",
    display_name_en="Skirt Type",
    id="skirtType",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/skirtType"),
    sub_property_of_uri=None,
    terms=None,
)
sleeveLength = CostumeCorePredicate(
    description_text_en="Each term that describes the length of the sleeves of the garment.",
    display_name_en="Sleeve Length",
    id="sleeveLength",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/sleeveLength"),
    sub_property_of_uri=None,
    terms=None,
)
sleeveType = CostumeCorePredicate(
    description_text_en="Each term that describes the shape of the sleeves of the garment.",
    display_name_en="Sleeve Type",
    id="sleeveType",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/sleeveType"),
    sub_property_of_uri=None,
    terms=None,
)
socioEconomicClass = CostumeCorePredicate(
    description_text_en="Each term that indicates the socioeconomic class of the person(s) who wore the object. This can have multiple values to show that the object was passed up or down through different classes.",
    display_name_en="Socio Economic Class",
    id="socioEconomicClass",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/socioEconomicClass"),
    sub_property_of_uri=None,
    terms=None,
)
spatial = CostumeCorePredicate(
    description_text_en="Where the item was originally made, if known; with all levels such as city, county, state, country, each as a separate entry.",
    display_name_en="Region",
    id="spatial",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/spatial"),
    sub_property_of_uri=None,
    terms=None,
)
startDate = CostumeCorePredicate(
    description_text_en="The earliest the garment could have been made, in the format YYYY or YYYY-MM or YYYY-MM-DD. Follow ISO 8601 standards.",
    display_name_en="Date Earliest",
    id="startDate",
    _uri=rdflib.term.URIRef("http://purl.org/vra/startDate"),
    sub_property_of_uri=None,
    terms=None,
)
storageLocation = CostumeCorePredicate(
    description_text_en='Where the garment has been put away in storage, for example by shelf section, ex. "C4"',
    display_name_en="Storage Location",
    id="storageLocation",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/storageLocation"),
    sub_property_of_uri=None,
    terms=None,
)
subject = CostumeCorePredicate(
    description_text_en='All costume artifacts should have the subject "Costume" or "Clothing and Dress." ',
    display_name_en="Subject",
    id="subject",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/subject"),
    sub_property_of_uri=None,
    terms=None,
)
temporal = CostumeCorePredicate(
    description_text_en='Each decade (or longer fashion style periods) in which the object was made or used. \n\nDo not include an apostrophe in a decade name; just add an "s," like "1950s."',
    display_name_en="Style Period",
    id="temporal",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/temporal"),
    sub_property_of_uri="http://purl.org/dc/terms/temporal",
    terms=None,
)
textileMaterials = CostumeCorePredicate(
    description_text_en="Each term for materials produced from component fibers, distinguished from the fibers, trimmings, or other materials.",
    display_name_en="Textile Materials",
    id="textileMaterials",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/textileMaterials"),
    sub_property_of_uri=None,
    terms=None,
)
title = CostumeCorePredicate(
    description_text_en="For costume artifacts that have not been titled by the original maker, this should be a descriptive phrase with about 3 important details, usually color, function, work type, or a notable detail.\n\nIn title case, less than 100 characters.",
    display_name_en="Title",
    id="title",
    _uri=rdflib.term.URIRef("http://purl.org/dc/terms/title"),
    sub_property_of_uri=None,
    terms=None,
)
treatment = CostumeCorePredicate(
    description_text_en="All procedures that have been completed to repair, conserve, stabilize, or display an object, in a narrative paragraph.",
    display_name_en="Treatment",
    id="treatment",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/treatment"),
    sub_property_of_uri=None,
    terms=None,
)
trimming = CostumeCorePredicate(
    description_text_en="Each term for decorative material added to an object, distinguished from the fibers, textile type,  or other materials.",
    display_name_en="Trimming",
    id="trimming",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/trimming"),
    sub_property_of_uri=None,
    terms=None,
)
type = CostumeCorePredicate(
    description_text_en='All clothing objects will have DCMI type "Physical Object." ',
    display_name_en="Type",
    id="type",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/type"),
    sub_property_of_uri="http://purl.org/dc/terms/type",
    terms=None,
)
underarmToWaistIn = CostumeCorePredicate(
    description_text_en="The measurement from armpit to waist at the side seam, in inches, as decimals to the nearest quarter inch.",
    display_name_en="Underarm To Waist",
    id="underarmToWaistIn",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/underarmToWaistIn"),
    sub_property_of_uri=None,
    terms=None,
)
waistIn = CostumeCorePredicate(
    description_text_en="The measurement straight around the narrowest part of the waist, in inches, as decimals to the nearest quarter inch.",
    display_name_en="Waist",
    id="waistIn",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/waistIn"),
    sub_property_of_uri=None,
    terms=None,
)
waistline = CostumeCorePredicate(
    description_text_en="Each term that describes the level and shape of the waist of the garment.",
    display_name_en="Waistline",
    id="waistline",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/waistline"),
    sub_property_of_uri=None,
    terms=None,
)
workType = CostumeCorePredicate(
    description_text_en="Each top-level work type of the object. More specific terms are possible as sub-categories, in other fields, or can be included in the description.",
    display_name_en="Work Type",
    id="workType",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/workType"),
    sub_property_of_uri=None,
    terms=None,
)
wornBy = CostumeCorePredicate(
    description_text_en="Full name(s) of anyone known to have worn a costume artifact.",
    display_name_en="Worn by",
    id="wornBy",
    _uri=rdflib.term.URIRef("https://w3id.org/costumeCore/ontology/wornBy"),
    sub_property_of_uri="http://www.wikidata.org/entity/P7376",
    terms=None,
)
COSTUME_CORE_PREDICATES = (
    alternative,
    cataloguerWithDate,
    cbLengthIn,
    cfLengthIn,
    chestIn,
    classification,
    closure,
    closurePlacement,
    collar,
    colorMain,
    colorSecondary,
    condition,
    conditionDescription,
    costOriginal,
    costumeComponents,
    creator,
    culturalContext,
    date,
    description,
    dimensionsOther,
    donator,
    dressType,
    endDate,
    exhibitions,
    extent,
    fiber,
    function,
    gender,
    hasInscription,
    hasTechnique,
    hemCircumferenceIn,
    hipsIn,
    icomType,
    identifier,
    isReferencedBy,
    length,
    lifeStages,
    liturgicalType,
    mannequin,
    material,
    neckline,
    otherMaterials,
    pantsType,
    pattern,
    placeOfRepository,
    privateInformation,
    publicInformation,
    relation,
    rights,
    rightsHolder,
    size,
    skirtType,
    sleeveLength,
    sleeveType,
    socioEconomicClass,
    spatial,
    startDate,
    storageLocation,
    subject,
    temporal,
    textileMaterials,
    title,
    treatment,
    trimming,
    type,
    underarmToWaistIn,
    waistIn,
    waistline,
    workType,
    wornBy,
)
