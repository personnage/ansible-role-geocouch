# Ansible Role: Geocouch for couchDB

[![Build Status](https://travis-ci.org/personnage/ansible-role-geocouch.svg?branch=master)](https://travis-ci.org/personnage/ansible-role-geocouch)

Installs Geocouch module for CouchDB database.

## Requirements

CouchDB instance.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    geocouch_inclide_js_test: true
    geocouch_version: "couchdb1.3.x"

## Dependencies

    - personnage.couchdb

## Example Playbook

    - hosts: webservers
      roles:
        - { role: personnage.geocouch }

## License

MIT / BSD

## Author Information

This role was created in 2016 by [The Personnage](https://github.com/personnage).
