window.TELIVU_CONFIG = Object.freeze({
  productVersion: "0.2.1", // Build refreshes from Directory.Build.props.
  downloadEnabled: false,
  releaseStatus: "", // Filled only after the public prerelease asset is verified.
  downloadUrl: "", // Approved public HTTPS release URL only.
  releaseNotesUrl: "resources/release-notes/",
  installerSize: "", // Size of the approved public release only.
  siteUrl: "", // Published root including project path and trailing slash.
  customDomain: "", // Host only; build generates CNAME when configured.
  contactUrl: "", // Approved HTTPS support URL or public mailto address.
  demoUrl: "", // Empty uses the honest demo placeholder.
  analytics: null // Reserved; no analytics scripts are loaded.
});
