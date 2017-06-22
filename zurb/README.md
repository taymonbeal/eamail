# Produces an email you can edit into a Django template

This is a pared-down fork of <https://github.com/rtanen/zurb-for-eamail> which is in turn a fork of <https://github.com/zurb/foundation-emails-template>. The purpose of this directory is to produce an HTML email that can then be converted into a Django template, as seen in `/project/subscriptions/templates/subscriptions/newsletter.html`.

**Warning:** Node has *not* been set up in the Vagrant virtual machine yet! Also, when you run this, it will download and assemble about 350MB of Node modules. These are covered by the `.gitignore`, but it's still something you probably don't want to be surprised by.

How to generate a Django template from this:

1. Run `npm run build`.
2. Find the file `/zurb/dist/index.html`. This is the file that you will turn into a Django template.
    * Check to make sure it does not reference external stylesheets and does have inlined CSS.
    * If you ran `npm build` instead of `npm run build`, you will not have the results you want.
3. Copy the contents of `/zurb/dist/index.html` to wherever you're making the Django template (probably `/project/subscriptions/templates/subscriptions/newsletter.html`).
4. Make the following straightforward replacements, which should be doable via a simple find-and-replace:
    * Remove the backslashes from the strings `{\{ event.name }}` and `{\{ event.location }}`.
    * Replace the text of the paragraph containing `{\{ event.description }}` and some lorem ipsum text with `{{ event.description }}`.
    * Replace the contents of the paragraph containing `<time>{\{ event.start_time }}</time>` with `<time datetime="{{ event.start_time|date:'c' }}">{{ event.start_time }}</time> {% if event.end_time %}: <time datetime="{{ event.end_time|date:'c' }}"> {{ event.end_time|timeuntil:event.start_time }} </time> long{% endif %}`, or whatever you're currently using to display the times.
    * Replace `img src="http://127.0.0.1:8000/media/17.jpg"` with `img src="http://127.0.0.1:8000{{ event.picture.url }}`.
    * Replace `a href="http://127.0.0.1:8000/event/3/"` with `a href="http://127.0.0.1:8000{% url 'event_detail' pk=event.pk %}"`.
5. Place the `{% for event in events %}` and `{% endfor %}` tags.
    * To find where to place the first of these tags, first find where `{{ event.name }}` is. Scroll up from there until you find the second-level table with the classes `container float-center`, right after the relatively contentless second-level table with the classes `spacer float-center`. Insert `{% for event in events %}` on the empty line between the table with the `spacer` class and the table with the `container` class.
    * To find where to place the second of these tags, first find where `{{ event.description }}` is. After this, there is some content, a blank line, another second-level table with the classes `spacer float-center`, followed by a blank line. On the blank line right after this second-level table with the `spacer` class, insert the `{% endfor %}` tag.
6. Steps which are probably optional, but I did them anyway:
    * Delete the empty line at the beginning of the file.
    * In the first second-level table of the file (the one with the style attribute giving it the background color `#054410`), replace all `color: #0a0a0a;` statements with `color: #ffffff;` statements.

Notes for putting this into production:

- There are several links to <http://127.0.0.1:8000>. This should be fixed.
- Currently, the unsubscribe link goes nowhere. We need to have a working one.
- Currently, we have a fake address of `EA Boston Events<br/>1024 E Main Street<br/>Somerville, MA 01234`. This needs to change.

Notes for editing this:

- Many things which appear to be changed by `src/assets/scss/_settings.scss` are not actually changed by it. Edit them manually in `_template.scss`. No, adding in variable names to `_template.scss` doesn't work. I'm not sure why.
- Inspecting the HTML output in a browser using "inspect elements" is useful for figuring out where to place the `{% for event in events %}` and `{% endfor %}` tags.
- You will want to reference other existing Zurb templates to make any major changes to this one. Some of those can be found at <https://github.com/zurb/foundation-emails-template>.

***

This is a fork of the official starter project for [Foundation for Emails](http://foundation.zurb.com/emails), a framework for creating responsive HTML devices that work in any email client. It has a Gulp-powered build system with these features:

- Handlebars HTML templates with [Panini](http://github.com/zurb/panini)
- Simplified HTML email syntax with [Inky](http://github.com/zurb/inky)
- Sass compilation
- Image compression
- Built-in BrowserSync server
- Full email inlining process

## Installation

To use this template, your computer needs [Node.js](https://nodejs.org/en/) 0.12 or greater. The template can be installed with the Foundation CLI, or downloaded and set up manually.

### Using the CLI

Install the Foundation CLI with this command:

```bash
npm install foundation-cli --global
```

Use this command to set up a blank Foundation for Emails project:

```bash
foundation new --framework emails
```

The CLI will prompt you to give your project a name. The template will be downloaded into a folder with this name.

### Manual Setup

To manually set up the template, first download it with Git:

```bash
git clone https://github.com/zurb/foundation-emails-template projectname
```

Then open the folder in your command line, and install the needed dependencies:

```bash
cd projectname
npm install
```

## Build Commands

Run `npm start` to kick off the build process. A new browser tab will open with a server pointing to your project files.

Run `npm run build` to inline your CSS into your HTML along with the rest of the build process.

Run `npm run litmus` to build as above, then submit to litmus for testing. *AWS S3 Account details required (config.json)*

Run `npm run mail` to build as above, then send to specified email address for testing. *SMTP server details required (config.json)*

Run `npm run zip` to build as above, then zip HTML and images for easy deployment to email marketing services.

### Speeding Up Your Build

If you create a lot of emails, your build can start to slow down, as each build rebuilds all of the emails in the
repository. A simple way to keep it fast is to archive emails you no longer need by moving the pages into `src/pages/archive`.
You can also move images that are no longer needed into `src/assets/img/archive`. The build will ignore pages and images that
are inside the archive folder.

## Litmus Tests (config.json)

Testing in Litmus requires the images to be hosted publicly. The provided gulp task handles this by automating hosting to an AWS S3 account. Provide your Litmus and AWS S3 account details in the `example.config.json` and then rename to `config.json`. Litmus config, and `aws.url` are required, however if you follow the [aws-sdk suggestions](http://docs.aws.amazon.com/AWSJavaScriptSDK/guide/node-configuring.html) you don't need to supply the AWS credentials into this JSON.

```json
{
  "aws": {
    "region": "us-east-1",
    "accessKeyId": "YOUR_ACCOUNT_KEY",
    "secretAccessKey": "YOUR_ACCOUNT_SECRET",
    "params": {
        "Bucket": "elasticbeanstalk-us-east-1-THIS_IS_JUST_AN_EXAMPLE"
    },
    "url": "https://s3.amazonaws.com/elasticbeanstalk-us-east-1-THIS_IS_JUST_AN_EXAMPLE"
  },
  "litmus": {
    "username": "YOUR_LITMUS@EMAIL.com",
    "password": "YOUR_ACCOUNT_PASSWORD",
    "url": "https://YOUR_ACCOUNT.litmus.com",
    "applications": ["ol2003","ol2007","ol2010","ol2011","ol2013","chromegmailnew","chromeyahoo","appmail9","iphone5s","ipad","android4","androidgmailapp"]
  }
}
```

## Manual email tests (config.json)

Similar to the Litmus tests, you can have the emails sent to a specified email address. Just like with the Litmus tests, you will need to provide AWS S3 account details in `config.json`. You will also need to specify to details of an SMTP server. The email address to send to emails to can either by configured in the `package.json` file or added as a parameter like so: `npm run mail -- --to="example.com"`

```json
{
  "aws": {
    "region": "us-east-1",
    "accessKeyId": "YOUR_ACCOUNT_KEY",
    "secretAccessKey": "YOUR_ACCOUNT_SECRET",
    "params": {
        "Bucket": "elasticbeanstalk-us-east-1-THIS_IS_JUST_AN_EXAMPLE"
    },
    "url": "https://s3.amazonaws.com/elasticbeanstalk-us-east-1-THIS_IS_JUST_AN_EXAMPLE"
  },
  "mail": {
    "to": [
      "example@domain.com"
    ],
    "from": "Company name <info@company.com",
    "smtp": {
      "auth": {
        "user": "example@domain.com",
        "pass": "12345678"
      },
      "host": "smtp.domain.com",
      "secureConnection": true,
      "port": 465
    }
  }
}
```

For a full list of Litmus' supported test clients(applications) see their [client list](https://litmus.com/emails/clients.xml).

**Caution:** AWS Service Fees will result, however, are usually very low do to minimal traffic. Use at your own discretion.
